import json

import requests

response = requests.get(url='https://fakerestapi.azurewebsites.net/api/v1/Authors')
print(response)
print(response.status_code)
# print(response.json())
# print(response.json().get('body'))

response = requests.get(url='https://fakerestapi.azurewebsites.net/api/v1/Authors/2')
print(response)
print(response.status_code)

response3 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Books/100')
print(response3)
print(response3.status_code)

response3 = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Users/100')
print(response3)
print(response3.status_code)


book_data = {
  "id": 1,
  "title": "abc",
  "description": "qqq",
  "pageCount": 100,
  "excerpt": "asdqwer",
  "publishDate": "2022-07-13T16:00:09.406Z"
}

json_data = json.dumps(book_data)

response3 = requests.put(url='https://fakerestapi.azurewebsites.net/api/v1/Books/1', data=json_data)
print(response3)
print(response3.status_code)


response3 = requests.delete(url='https://fakerestapi.azurewebsites.net/api/v1/Users/4')
print(response3)
print(response3.status_code)
