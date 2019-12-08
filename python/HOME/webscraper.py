from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.homemcr.org/theatre/'
hdr = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=hdr)
content = BeautifulSoup(response.content, "html.parser")
fullContent = []

for show in content.find_all('article'):
    try:
            showObject = {
        "name": show.find('h3').get_text(strip=True),
        "info": show.find('header').get_text(strip=True),
        "more-info": show.find('div', attrs={"class" : "tile-body"}).get_text(strip=True)
        }
            fullContent.append(showObject)
            with open('home.json', 'w') as outfile:
                json.dump(fullContent, outfile)

    except:
        pass

