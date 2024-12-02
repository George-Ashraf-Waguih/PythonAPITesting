import json
import requests
import jsonpath

def test_oauth_api():
    token_url = 'http://thetestingworldapi.com/Token'
    data = {'grant_type':'password','username':'admin','password':'password'}
    response = requests.post(token_url, data=data)
    token_value = response.json()['token']

    auth = {'Authorization':'Bearer'+ token_value}
    API_URL = 'http://thetestingworldapi.com/api/authentication'
    response = requests.get(API_URL, headers=auth)
    print(response.json())

