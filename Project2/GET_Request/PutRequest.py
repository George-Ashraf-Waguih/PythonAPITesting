import requests
import json
import jsonpath


url = 'https://reqres.in/api/users/2'

# Read Input Json file
file = open('/Users/macbookpro/Desktop/Projects/BackendAutomation/BackendAutomation/Project2/CreateUser.json','r')
json_input = file.read()
request_json = json.loads(json_input)

# print(request_json)

# Make PUT request with Json Input body
response = requests.put(url, json=request_json)
print(response.status_code)
assert response.status_code == 200
print(response.json())

# Fetch header from response
print(response.headers)
print(response.headers['Content-Type'])

# Parse response to Json format
response_json = json.loads(response.text)

# Pick updatedAt using JSON Path
updatedAt = jsonpath.jsonpath(response_json,'updatedAt')
print(updatedAt[0])