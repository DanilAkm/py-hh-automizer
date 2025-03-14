# https://api.hh.ru/openapi/redoc#section/Avtorizaciya/Process-avtorizacii

import requests
import json
import common

TOKEN_URL = f'{common.HH_API_BASE}/token'

def get_app_token(client_id: str, client_secret: str) -> dict:
  """!Method returns a new application token to authorize the application

  @param client_id     Client_id from dev.hh.ru/admin.
  @param client_secret Client_secret from dev.hh.ru/admin.

  @return Json (dict) with token, None in case of an error
  """
  data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
  }

  try:
    response = requests.post(url=TOKEN_URL, data=data)
    if response.status_code != 200:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None
  
  return response.json()

def get_user_access_token(client_id: str, client_secret: str, auth_code: str) -> dict:
  """!Returns a dict containing user's access token, refresh token and expiration time

  @param client_id     Client_id from dev.hh.ru/admin.
  @param client_secret Client_secret from dev.hh.ru/admin.
  @param auth_code     The code returned from hh.ru after the user authenticates on hh.ru/oauth/authorize?response_type=code&client_id={client_id}. Check https://api.hh.ru/openapi/redoc#section/Avtorizaciya/Zapros-avtorizacii-pod-drugim-polzovatelem

  @return Json (dict) with access_token, refresh_token and expiration time. None in case of an error
  """
  
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }

  data = {
    'code': auth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'authorization_code'
  }

  try:
    response = requests.post(url=TOKEN_URL, headers=headers ,data=data)
    if response.status_code != 200:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None

  return response.json()

def refresh_access_token(refresh_token: str) -> dict:
  """!Returns a dict containing user's new access token, refresh token and expiration time

  @param refresh_token Refresh token of an expired access token.

  @return Json (dict) with access_token, refresh_token and expiration time. None in case of an error
  """
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  data = {
    'refresh_token': refresh_token,
    'grant_type': 'refresh_token'
  }

  try:
    response = requests.post(url=TOKEN_URL, headers=headers, data=data)
    if response.status_code != 200:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None
  return response.json()

def invalidate_token(access_token: str) -> dict:
  """!Invalidates the access token as well the refresh_token

  @param access_token

  @return dict
  """

  headers = {
    'Authorization': f'Bearer {access_token}'
  }

  try:
    response = requests.delete(url=TOKEN_URL, headers=headers)
    if response.status_code != 204:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None

  return response.json()

if __name__ == '__main__':
  print(get_app_token('IQ16DUSQ78T2KNQIKA8VVED1SGT1M34UBRNR5QHH5B1654E2NRR87MNM246Q32LC', 'MLOO81QQ87T1EN482OICAG5TCT137KRPBP7SIBLJHL49EA99V5VT055QRED24DMA'))
