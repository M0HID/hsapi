# High-Seas (unofficial) API

Returns a JSON object of all the items in the shop, including prices, regions, and stock

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

## Usage
To run the api, just run the following command:
```uvicorn api:app --reload```

You can now access the API at `localhost:8000/hsapi`