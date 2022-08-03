# main.py

from datetime import datetime
import json
from typing import Union
import requests
from fastapi import FastAPI, Depends
from pydantic import BaseModel, HttpUrl
import jwt
from fastapi.security import HTTPBearer
from time import time, ctime
reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)
app = FastAPI()

class Meeting(BaseModel):
    agenda: str
    default_password: bool
    duration: int
    password: str
    pre_schedule: bool
    start_time: str
    template_id: str
    timezone: str
    topic: str
    type: int


API_KEY = 'VHJ2UiubSpqShrrbwu-3Uw'
API_SEC = 'O2E69V0NofenJS9lFjVMrz7DFcun5RV69BNZ'

def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing
        # API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 30000},
        API_SEC,
        algorithm='HS256'
    )
    print(token, 444)
    print("can you clone repo automatically?")
    return token.decode('utf-8')

@app.get("/user")
def get_user(email: str):
    url = f"https://api.zoom.us/v2/users/{email}/"
    headers = {
        "Authorization": f"Bearer {generateToken()}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/meetinglist")
def get_meeting_list(email: str):
    url = f"https://api.zoom.us/v2/users/{email}/meetings/"
    headers = {
        "Authorization": f"Bearer {generateToken()}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/singlemeeting")
def get_a_meeting(meetingId):
    url = f"https://api.zoom.us/v2/meetings/{meetingId}"
    headers = {
        "Authorization": f"Bearer {generateToken()}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.get("/record")
def get_record(meetingId):
    url = f"https://api.zoom.us/v2/meetings/{meetingId}/recordings"
    headers = {
        "Authorization": f"Bearer {generateToken()}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.post("/meeting")
async def create_meeting(email: str, data: Meeting):
    url = f"https://api.zoom.us/v2/users/{email}/meetings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {generateToken()}"
    }
    print('type: ', type(data.dict()))
    response = requests.post(url, headers=headers, json=data.dict())
    print('res: ', response)
    print('res: ', response.json())
    return response.json()