import asyncio
import json
import re
import string
import random
import pytest
import websockets
import uuid


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + "-_"
    return ''.join(random.choice(characters) for i in range(length))


TOKEN = generate_random_string(1273)
URI = 'wss://rm.picfinder.dev/'


def generate_uuid():
    return str(uuid.uuid4()).lower()


def new_connection_message(token):
    return {
        "newConnection": {
            "ws": "https://picfinder.ai/",
            "securityToken": token,
        }
    }


def new_task_uuid_message(old_task_uuid):
    return {
        "newTaskUUID": {
            "oldTaskUUID": old_task_uuid
        }
    }


def validate_new_task_response(response):
    assert response is not None
    assert 'error' not in [_.lower() for _ in response.keys()]
    assert 'newTaskUUID' in [_ for _ in response.keys()]
    assert 'taskUUID' in response['newTaskUUID'].keys()
    assert re.match(r'^[a-f\d]{8}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{4}-[a-f\d]{12}$',
                    response['newTaskUUID']['taskUUID'])


def validate_text_2_img_response(response):
    assert response is not None
    assert 'error' not in [_.lower() for _ in response.keys()]
    assert 'newImages' in [_ for _ in response.keys()]
    assert 'images' in response['newImages'].keys()
    assert len(response['newImages']['images']) >= 1
    for image in response['newImages']['images']:
        assert 'imageSrc' in image.keys()
        assert 'imageUUID' in image.keys()


async def bypass_total_number_of_images_and_receive(message, wss_uri):
    cnt = 0
    while cnt <= 5:
        try:
            async with websockets.connect(wss_uri) as websocket:
                while True:
                    await websocket.send(json.dumps(message))
                    print('Sent', json.dumps(message))
                    response = await websocket.recv()
                    print('Received', json.loads(response))
                    response_json = json.loads(response)
                    # Check if the response does not contain keys we can't use
                    if not any(
                            unwanted_resp in response_json.keys() for unwanted_resp in ['abs', 'totalNumberOfImages']):
                        websocket.close()
                        yield response_json
                        break
        except websockets.ConnectionClosedError:
            print('WebSocket connection closed. Retrying...')
            await asyncio.sleep(1)
            cnt += 1
        except Exception as e:
            print(f'Error:a {e}')
            break


# this is not tested
async def send_and_receive(message_list, wss_uri, target_key):
    async with websockets.connect(wss_uri) as websocket:
        # Write each message in the list to the WebSocket
        for message in message_list:
            await websocket.send(json.dumps(message))
        # Wait for messages until one contains the target key
        while True:
            response_json = await websocket.recv()
            response_data = json.loads(response_json)
            if target_key in response_data:
                break
    yield response_data


@pytest.mark.asyncio
async def test_websocket_handshake_generates_taskuuid():
    async with websockets.connect(URI) as websocket:
        message = new_connection_message(TOKEN)
        message_json = json.dumps(message)
        await websocket.send(message_json)
        response = await websocket.recv()
        response_js = json.loads(response)
        while 'totalNumberOfImages' in response_js.keys():
            await websocket.send(message_json)
            response = await websocket.recv()
            response_js = json.loads(response)
        print(response_js)
        validate_new_task_response(response_js)


@pytest.mark.asyncio
async def test_can_get_new_uuid():
    message = new_connection_message(TOKEN)
    response = await bypass_total_number_of_images_and_receive(message, URI).__anext__()
    validate_new_task_response(response)
    old_task_uuid = response['newTaskUUID']['taskUUID']
    new_message = new_task_uuid_message(old_task_uuid)
    new_response = await bypass_total_number_of_images_and_receive(new_message, URI).__anext__()
    validate_new_task_response(new_response)
    new_task_uuid = new_response['newTaskUUID']['taskUUID']
    assert old_task_uuid != new_task_uuid


async def send_new_images_request(startingPage, promptText, numberResults, sizeId, taskType):
    message = new_connection_message(TOKEN)
    response = await bypass_total_number_of_images_and_receive(message, URI).__anext__()
    validate_new_task_response(response)
    task_uuid = response['newTaskUUID']['taskUUID']
    new_message = {
        "newTask": {"taskUUID": f"{task_uuid}", "startingPage": startingPage, "promptText": f"{promptText}",
                    "numberResults": numberResults, "sizeId": sizeId, "taskType": taskType}}
    new_image_response = await bypass_total_number_of_images_and_receive(new_message, URI).__anext__()
    validate_text_2_img_response(new_image_response)
    yield new_image_response


@pytest.mark.asyncio
async def test_can_get_new_image_from_text_prompt():
    desired_results = random.randint(1, 7)
    response = await send_new_images_request(0, 'gaga', desired_results, 1, 1).__anext__()
    assert len(response['newImages']['images']) == desired_results
