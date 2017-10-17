from bs4 import BeautifulSoup
import urllib.request

url = "https://allabolag.se/what/a?page=1"
req = urllib.request.urlopen(url)
soup = BeautifulSoup(req, 'html.parser')

for link in soup.find_all('a'):
    try:
        url = link.get('href')
        req = urllib.request.urlopen(url)
        soup = BeautifulSoup(req, 'html.parser')
    except ValueError:
        print('value error:', url)

    table = soup.find('table', {"class" : "figures-table"})
    if table:
        print(table)
