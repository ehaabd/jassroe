import requests
from bs4 import BeautifulSoup as bs

 
def readMainText(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    s = soup.find('div', class_='entry-content')
    lines = s.find_all('p')
    completeText = ''
    
    for line in lines:
        completeText += line.text
    
    return completeText