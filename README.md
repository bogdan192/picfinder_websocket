# Smoke tests for picfinder websocket

Tests the new UUID generation, replacing an UUID and requesting and receiving
images from strings
Requires python 3


 

## How to install

- python3 -m pip install -r requirements.txt

## How to run
python3 -m pytest --html=report.html --self-contained-html tests.py

## Warnings
The tests generate a lot of SSL related warnings. Still haven't gotten around to fix those

## check_connection script
The script is a simple program to connect to the ws. You can use it to spy on ws activity
No real-world use other than testing it can be done.
