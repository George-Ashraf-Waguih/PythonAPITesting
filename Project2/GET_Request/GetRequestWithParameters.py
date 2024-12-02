import requests

param = {'name':'Geo', 'email':'test@test.com', 'number':'123456'}
response = requests.get('https://httpbin.org/get', params=param)
print(response.text)