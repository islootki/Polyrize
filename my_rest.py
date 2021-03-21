#pip install requests
import json
import requests


class ApiError(Exception):
    pass
'''
The requast failed on {'Content-Length': '67', 'Content-Type': 'application/json', 'Connection': 'keep-alive', 'Keep-Alive': '5'}
'''
url = 'http://localhost:8000/api/auth'
body = {"username": "test", "password": "1234"}
resp = requests.post(url, data=json.dumps(body))

if resp.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))
