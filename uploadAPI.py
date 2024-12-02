import requests

url = 'https://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

r = requests.post(url,files=files)
r.text
