import requests
from bs4 import BeautifulSoup

li = []
data = requests.get('https://rahulshettyacademy.com/AutomationPractice/')
soup = BeautifulSoup(data.content, 'html.parser')
appium = soup.find('a',string='Appium')
print(appium['href'])
