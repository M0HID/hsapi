# High-Seas (unofficial) API

Returns a JSON object of all the items in the shop, including prices, regions, and stock. Try it out [here](https://m0hid--hsapi-fastapi-app.modal.run/hsapi?next_action=24c833d8076ace77d8754d64382e8f126f9b3564)!

## Dependencies
- FastAPI
- curl
- uvicorn
- python

## Installation
(Only supported on Linux for now!!)

1. Clone the repo:
```git clone https://github.com/M0HID/hsapi```

2. Navigate to the project dir
```cd hsapi```

3. Install packages
```pip install fastapi uvicorn```

4. Get your hs-session token from https://highseas.hackclub.com/shop and export it to HS_SESSION_TOKEN

5. Get the current next-action by inspecting the network traffic - its in a request called 'shop'

## Usage
To run the api, just run the following command:
```python3 api.py```

You can now access the API at `localhost:8000/hsapi`
