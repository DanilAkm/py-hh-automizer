import requests
import json
import common

def showme(access_token: str, client_info: str, host='hh.ru', locale='ru') -> dict:
  """! /me call to get user profile info

  @param access_token
  @param client_info App name and developer's contact email. ex. MyApp/1.0 (my-app-feedback@example.com)
  @param host url of your app
  @param locale localization - two letter code

  @return dict with user info
  """
  
  headers = {
    'Authorization': f'Bearer {access_token}',
    'HH-User-Agent': client_info 
  }

  params = {
    'locale': locale,
    'host': host
  }

  URL=f'{common.HH_API_BASE}/me'

  try:
    response = requests.post(url=URL, headers=headers, params=params)
    if response.status_code != 200:
      print(response.json())
      return None
    return response.json()
  except Exception as e:
    print(e)
    return None
