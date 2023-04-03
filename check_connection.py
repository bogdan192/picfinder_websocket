import websocket
import json
import uuid

def generate_uuid():
    return str(uuid.uuid4()).lower()

def on_message(ws, message):
    if 'totalNumberOfImages' not in json.loads(message).keys():
        print("Received: ",  json.loads(message))

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print(f"Websocket connection closed with status code {close_status_code}: {close_msg}")

def on_open(ws):
    print("Established connection")

#     message = {
# 	"newTask": {
# 		"taskUUID": "7a08ba1f-53b8-4b1d-9882-7b39649547ba",
# 		"startingPage": 0,
# 		"promptText": "dad",
# 		"numberResults": 6,
# 		"sizeId": 1
# 	}
# }

    message  = {
	"newTask": {
		"taskUUID": "4f48fed7-fd34-4fac-8c97-0f5bf809d12f",
		"startingPage": 0,
		"promptText": "gaga",
		"numberResults": 6,
		"sizeId": 1,
		"taskType": 1
	}
}

    # message = {
    #     "newConnection": {
    #         "taskUUID": f"{generate_uuid()}",
    #         "ws": "https://picfinder.ai/",
    #         "apiKey": "03AKH6MREdzCo0vk11FdYYONpuFpD7-vvhmnVkcU5sVgkw-z1jdiIzTdda8pxlk5-CWDFmT9VDRnc5lo7LFj4c-x7ZXflxusoyWL5s4qEAiN25xuZLcllK3tB1CdlCHCyqmxd8rnFh9nDLeWy0d2YGiYxEKjQVX4hVSuwqmqXjHJMVJ63PRfeO-EUGsDBharRSwJ0-DwCXN1tKvq-4zB2200337sFsDLOi7xnidXD2l4grk2e2MqBdCpGqmAbWrzl8K2tm5K3IEUcMK_aq3aPJ-KUE5YF7n4QAiw2Lx83kFxkShYHafUzDMqQDZgvWhUpPOWc3h5Ev-1XTyCbN_yrJ6MuLbwgfPKSQ8LKPjOaOa9ZKMEZruenyU-Way7iG3a7hrzmB6xXQK5Sb8aErwIcGcjnyLEkRyeZRo-Xo48SdiTFo6h-1KNcgBJlzmTatZlP7Nb6FoVR79d7tyvb1yNr3Mn6luqb5PxCcaQKjMkKvAyYnDX-h1t27RdDrf5nkYwZ2au2Gf03j6eip8kzjlwthuO-HtNpEK_0zBLEQeMB7N1Zel1TAwhG5qo7kwv6KMlNTCIs_yMexp2iwvpNolDs6xr9wPi0dCzbaofv-Jeqn-3f64Onv9wNQrXLphCdu9lEBUCnqJJStKcCEdgJfuJYpxHrXRAy9IvOhIqbMsgt1HYK3JRsuqABnOhWgghp9bAguoM5Vp9k222ne4sMnxaA9VRWD81RKtdcbPNNLKmDvz3VOuvZFisyT4NnSJc7W_7h-sbbCweZJrjgAo17w3vBklluv1JLfe_alxS46ySOjlx8XwAXxYJEZaVvmp6z-hfn4dbIQBZPT3_72l93GWsOM24xuSLBn-2k0uNADSamzXaxlZasODF6KVtEK2Gz6M1nMrJTH_3ROF3ICtx1SmyH6_P6SL3sS2OST8XWoe9uyYIJxJ0d-jDQ8h3ilkkdtRNl1wkuVLRVxsEINXrTka-raKcm_ZjC_hV7-yNYMi2p-yLzjhd5nNgFSGsqeewNUu8bxQMpsvk_3tKXKHW4vFL0tm1_aHHlj5pvfdm9S6X-PhhoOUbc7YhXhpq_85fUkm8Y5pSnvb5BezN5-uOGt1LWM-qlvPBUeTsWxPq72rUmQsIxwcssHvfLlMOVNmoILPkVJ2KEj3ElUBxUbeQV2zklcB_TtNS8eAS0LUD1X7eDptZjH3LgNDUbzoiq9d9KwMGkvkd85xFeNrTt8WqGByB2SCKArtkwXa_KhgyxOp7pwviK90P-dGrpwNlE"
    #     }
    # }
    #
    # message = {
    # "newConnection": {
    #     "apiKey": "03AKH6MREdzCo0vk11FdYYONpuFpD7-vvhmnVkcU5sVgkw-z1jdiIzTdda8pxlk5-CWDFmT9VDRnc5lo7LFj4c-x7ZXflxusoyWL5s4qEAiN25xuZLcllK3tB1CdlCHCyqmxd8rnFh9nDLeWy0d2YGiYxEKjQVX4hVSuwqmqXjHJMVJ63PRfeO-EUGsDBharRSwJ0-DwCXN1tKvq-4zB2200337sFsDLOi7xnidXD2l4grk2e2MqBdCpGqmAbWrzl8K2tm5K3IEUcMK_aq3aPJ-KUE5YF7n4QAiw2Lx83kFxkShYHafUzDMqQDZgvWhUpPOWc3h5Ev-1XTyCbN_yrJ6MuLbwgfPKSQ8LKPjOaOa9ZKMEZruenyU-Way7iG3a7hrzmB6xXQK5Sb8aErwIcGcjnyLEkRyeZRo-Xo48SdiTFo6h-1KNcgBJlzmTatZlP7Nb6FoVR79d7tyvb1yNr3Mn6luqb5PxCcaQKjMkKvAyYnDX-h1t27RdDrf5nkYwZ2au2Gf03j6eip8kzjlwthuO-HtNpEK_0zBLEQeMB7N1Zel1TAwhG5qo7kwv6KMlNTCIs_yMexp2iwvpNolDs6xr9wPi0dCzbaofv-Jeqn-3f64Onv9wNQrXLphCdu9lEBUCnqJJStKcCEdgJfuJYpxHrXRAy9IvOhIqbMsgt1HYK3JRsuqABnOhWgghp9bAguoM5Vp9k222ne4sMnxaA9VRWD81RKtdcbPNNLKmDvz3VOuvZFisyT4NnSJc7W_7h-sbbCweZJrjgAo17w3vBklluv1JLfe_alxS46ySOjlx8XwAXxYJEZaVvmp6z-hfn4dbIQBZPT3_72l93GWsOM24xuSLBn-2k0uNADSamzXaxlZasODF6KVtEK2Gz6M1nMrJTH_3ROF3ICtx1SmyH6_P6SL3sS2OST8XWoe9uyYIJxJ0d-jDQ8h3ilkkdtRNl1wkuVLRVxsEINXrTka-raKcm_ZjC_hV7-yNYMi2p-yLzjhd5nNgFSGsqeewNUu8bxQMpsvk_3tKXKHW4vFL0tm1_aHHlj5pvfdm9S6X-PhhoOUbc7YhXhpq_85fUkm8Y5pSnvb5BezN5-uOGt1LWM-qlvPBUeTsWxPq72rUmQsIxwcssHvfLlMOVNmoILPkVJ2KEj3ElUBxUbeQV2zklcB_TtNS8eAS0LUD1X7eDptZjH3LgNDUbzoiq9d9KwMGkvkd85xFeNrTt8WqGByB2SCKArtkwXa_KhgyxOp7pwviK90P-dGrpwNlE",
    #         "taskUUID": f"f{generate_uuid()}"
    #     }
    # }
    message_json = json.dumps(message)
    ws.send(message_json)


if __name__ == "__main__":
    websocket_url = "wss://rm.picfinder.dev/"
    ws = websocket.WebSocketApp(websocket_url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
