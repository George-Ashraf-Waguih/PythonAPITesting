import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send Get Request
response = requests.get(url)
print(response)

# Display Response content
print(response.content)
print(response.json())

# Validate status code
print(response.status_code)
assert response.status_code == 200

# Fetch Response Header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))
print(response.headers.get('Content-Type'))

# Fetch Cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

# Fetch Elapsed Time
print(response.elapsed)

# Parse response in json
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0]) # 2
assert pages[0] == 2

first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name[0])
assert first_name[0] == "Michael"

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response, f'data[{i}].first_name')
    print(first_name[0])