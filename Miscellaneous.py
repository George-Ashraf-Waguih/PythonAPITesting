import requests

#http://rahulshettyacademy.com  url
#'visit-month   cookie used

# allow_redirects=False to cancel redirection in request
# timeout=1 for wait in requests to load

cookie = {'visit-month':'February'}
response = requests.get('http://rahulshettyacademy.com',allow_redirects=False,cookies=cookie,timeout=1)
# redirection first gets 302 before redirecting to the target url giving 200
print(response.history)
print(response.status_code)

url = 'https://httpbin.org/cookies'
se = requests.session()
se.cookies.update({'visit-month':'February'})
response1 = se.get(url,cookies=cookie)
print(response1.json())

# Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('random-pic.jpg','rb')}
response2 = requests.post(url,files=files)
print(response2.status_code)
print(response2.text)
