# Required imports
import requests
import os
from dotenv import load_dotenv

# Load environment variables
from pathlib import Path
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

# Backend URLs from .env
backend_url = os.getenv(
    'backend_url',
    default="http://localhost:3030"
)

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)


# ---------------------------------------
# GET REQUEST TO BACKEND
# ---------------------------------------
def get_request(endpoint, **kwargs):
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + value + "&"

    request_url = backend_url + endpoint
    if params:
        request_url += "?" + params

    print("GET from {}".format(request_url))

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# ---------------------------------------
# SENTIMENT ANALYSIS MICROSERVICE
# ---------------------------------------
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# ---------------------------------------
# POST REVIEW TO BACKEND
# ---------------------------------------
def post_review(data_dict):
    request_url = backend_url + "/insert_review"

    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")