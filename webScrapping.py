import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.imdb.com/find/?q=thriller&ref_=nv_sr_sm')
soup = BeautifulSoup(data.content, 'html.parser')
print(soup.prettify())

moviesTable = soup.find('div', attrs={'class': 'lister-item'})
print(moviesTable.prettify())

rows = moviesTable.findAll('tr')
for row in rows:
    rowData = row.findall('td')
    rowData[1].findAll('a')
    print(rowData[1].find('a').text)
    subUrl = rowData[1].a['href']
    subData = requests.get('https://www.imdb.com'+subUrl)
    childsoup = BeautifulSoup(subData.content, 'html.parser')
    if childsoup.find('div', attrs={'class': 'lister-item'}):
        genre = childsoup.find('div', attrs={'class': 'lister-item'})
        if genre.find('a') == " Documentry":
            print(rowData[1].find('a').text)
            print(genre.find('a').text)

    
