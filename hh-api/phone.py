import common
import requests
import json

def confirm_phone(access_token: str, client_info: str, host: str, phone: str, confirmation_code: str, locale='ru') -> dict:
  """! /resume_phone_confirm - needs extra parametres from a form in your website:
  @param access_token
  @param client_info App name and developer's contact email. ex. MyApp/1.0 (my-app-feedback@example.com)
  @param host url of your app
  @param locale localization - two letter code

  @return dict
  """

  headers = {
    'Authorization': f'Bearer {access_token}',
    'HH-User-Agent': client_info 
  }

  params = {
    'locale': locale,
    'host': host
  }

  json_data = {
    'phone': phone,
    'confirmation_code': confirmation_code
  }

  URL=f'{common.HH_API_BASE}/resume_phone_confirm'

  try:
    response = requests.post(url=URL, headers=headers, params=params, json=json_data)
    if response.status_code != 200:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None
  
  return response.json()

def get_phone_info(access_token: str, client_info: str, host: str, phone: str, locale='ru') -> dict:
  """! /resume_should_send_sms get phone number info
  @param access_token
  @param client_info App name and developer's contact email. ex. MyApp/1.0 (my-app-feedback@example.com)
  @param host url of your app
  @param phone in any format?
  @param locale localization - two letter code
  """

  headers = {
    'Authorization': f'Bearer {access_token}',
    'HH-User-Agent': client_info 
  }

  params = {
    'locale': locale,
    'host': host,
    'phone': phone
  }


  URL=f'{common.HH_API_BASE}/resume_should_send_sms'

  try:
    response = requests.get(url=URL, headers=headers, params=params)
    if response.status_code != 200:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None

def send_confirmation_code(access_token: str, client_info: str, host: str, phone: str, locale='ru') -> dict:
  """!/resume_phone_generate_code send confirmaation code
  
  @param access_token
  @param client_info App name and developer's contact email. ex. MyApp/1.0 (my-app-feedback@example.com)
  @param host url of your app
  @param phone in any format?
  @param locale localization - two letter code

  @return dict
  """
  headers = {
    'Authorization': f'Bearer {access_token}',
    'HH-User-Agent': client_info 
  }

  params = {
    'locale': locale,
    'host': host
  }

  data = {
    'phone': phone
  }

  URL=f'{common.HH_API_BASE}/resume_phone_generate_code'

  try:
    response = requests.post(url=URL, headers=headers, params=params, data=data)
    if response.status_code != 200:
      print(response.json())
      return None
  except Exception as e:
    print(e)
    return None
  
  return response.json()
