import requests
import json
import jsonpath
import pytest


url = 'https://reqres.in/api/users'
a=10

@pytest.fixture(scope='module')
def start_exec():
    global file
    file = open('/Users/macbookpro/Desktop/Projects/BackendAutomation/BackendAutomation/Project2/CreateUser.json', 'r')

@pytest.mark.skipif(a>10,reason='condition not satisfied')
def test_create_new_user(start_exec):
    json_input = file.read()
    request_json = json.loads(json_input)
    # print(request_json)
    # Make post request with Json Input body
    response = requests.post(url, json=request_json)
    print(response.status_code)
    assert response.status_code == 201
    print(response.json())
    # Fetch header from response
    print(response.headers)
    print(response.headers['Content-Length'])
    # Parse response to Json format
    response_json = json.loads(response.text)
    # Pick ID using JSON Path
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])

def test_create_other_user(start_exec):
    # Read Input Json file
    file = open('/Users/macbookpro/Desktop/Projects/BackendAutomation/BackendAutomation/Project2/CreateUser.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # print(request_json)
    # Make post request with Json Input body
    response = requests.post(url, json=request_json)
    print(response.status_code)
    assert response.status_code == 201
    print(response.json())
    # Fetch header from response
    print(response.headers)
    print(response.headers['Content-Length'])
    # Parse response to Json format
    response_json = json.loads(response.text)
    # Pick ID using JSON Path
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])