import requests
import json

HH_API_BASE_URL = 'https://api.hh.ru'


def define_profession(mask = '') -> json:
  data = None
  found_roles = []
  data = requests.get(url='https://api.hh.ru/professional_roles').json()
  if len(mask) == 0:
    return data
  else:
    for category in data['categories']:
      for role in category['roles']:
        if mask in role['name'].lower():
          found_roles.append(role)
    return found_roles
    
    

def find(profession_code: int, query: str, records: int) -> json:
  endpoint = 'vacancies'
  params = {
    "professional_role": profession_code,
    "text": query,
    "per_page": records
  }
  response = requests.get(f"{HH_API_BASE_URL}/{endpoint}", params=params)
  
  return response.json()

res = define_profession('водитель') # find(165, 'data scientist', 20)

print(json.dumps(res, indent=4, ensure_ascii=False))