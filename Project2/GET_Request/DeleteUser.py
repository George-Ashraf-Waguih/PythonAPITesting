import requests
from datetime import timedelta

url = 'https://reqres.in/api/users/2'

response = requests.delete(url)

print(response.status_code)
assert response.status_code == 204

print(response.elapsed)
assert response.elapsed < timedelta(seconds=1), f'Response time {response.elapsed} seconds ago'
