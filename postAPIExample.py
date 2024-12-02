import requests
from payLoad import *
# import configparser
from utilities.configurations import *
from utilities.resources import *

# config = getConfig()
# Add book

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers={"Content-type":"'application/json"}
query = 'select * from Books'
addBook_response = requests.post(url,json=buildPayLoadFromDB(query), headers=headers,)

print(addBook_response.json())
print(addBook_response.status_code)
response_json = addBook_response.json()

bookID = response_json['ID']
print(bookID)

# Delete book
url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
json={

"ID" : bookID

}
response_delete = requests.post(url,json=json,headers=headers,)
print(response_delete.status_code) # 200
assert response_delete.status_code == 200
print(response_delete.json())
res_del_json = response_delete.json()
print(res_del_json['msg'])
assert res_del_json['msg'] == 'book is successfully deleted'


# Authentication

url = "https://api.github.com/user"
github_response = requests.get(url, verify=False, auth=('George-Ashraf-Waguih',getPassword()))
print(getPassword())
print(github_response.status_code)

# Session Managing
se = requests.session()
se.auth = auth=('George-Ashraf-Waguih',getPassword())

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)
print(response.json())
