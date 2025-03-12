from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import json
import requests
import os
import sys
from dotenv import load_dotenv # type: ignore
# import apply.login

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from apply.login import get_user_auth_token

load_dotenv('../.env')
client_id = os.getenv('CLIENT_ID')

app = FastAPI()

HH_OAUTH_URL = "https://hh.ru/oauth/authorize"
 
@app.get("/login")
def login():
    return RedirectResponse(f"{HH_OAUTH_URL}?response_type=code&client_id={client_id}")

@app.get("/oauth")
def oauth_callback(request: Request, code: str):
    print(f"Received OAuth code: {code}")
    auth_token = get_user_auth_token(code)
    print(auth_token)
    headers = {
       "Authorization": f"Bearer {auth_token['access_token']}",
       'HH-User-Agent': 'boyceing.ru/1.0 boyceing@boyceing.ru'
    }
    info = requests.get('https://api.hh.ru/me', headers=headers)
    user_data_json = json.dumps(info.json())
    encoded_user_data = requests.utils.quote(user_data_json)
    return RedirectResponse(f"https://boyceing.ru?user={requests.utils.quote(str(encoded_user_data))}")
