import requests
import json
import os
from dotenv import load_dotenv # type: ignore

load_dotenv('../.env')
client_id = os.getenv('CLIENT_ID')
client_secret= os.getenv('CLIENT_SECRET')

def get_access_token(cleint_id: str, client_secret: str, grant_type='client_credentials'):
  params = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': grant_type 
  }
  response = requests.post(url='https://api.hh.ru/token', params=params)
  return response.json()

def get_user_auth_token(auth_code: str):
  load_dotenv('../.env')
  client_id = os.getenv('CLIENT_ID')
  client_secret= os.getenv('CLIENT_SECRET')
  
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }

  params = {
    'code': auth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code'
  }

  response = requests.post(url=' https://api.hh.ru/token', headers=headers ,params=params)
  return response.json()


if __name__ == '__main__':
    print('idi nahui')
