import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'RahulShetty2'},)

print(response.text)
print(type(response.text))
print(response.json())
print(response.status_code)

dict_response = json.loads(response.text)
print(dict_response)
print(type(dict_response))
print(dict_response[0]['isbn'])

json_response = response.json()

print(response.status_code)
assert response.status_code == 200

print(response.headers)
print(response.headers['Content-type'])
assert response.headers['Content-type'] == 'application/json;charset=UTF-8'

print(response.cookies)
# assert response.cookies == []

# Retrieve the book details with isbn = bcdds
response1 = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'RahulShetty'},)
json_response1 = response1.json()

expectedBook =  {
        "book_name": "Appium Automation with Java",
        "isbn": "QABC",
        "aisle": "288"
    }

for book in json_response1:
    if book['isbn'] == 'QABC':
        print(book)
        break

assert book == expectedBook


