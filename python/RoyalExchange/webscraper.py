from bs4 import BeautifulSoup
import requests
import json

url = 'https://bookings.royalexchange.co.uk/overview/'
show = 'gypsy20192020'
fullUrl = url + show
hdr = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(fullUrl, headers=hdr)
content = BeautifulSoup(response.content, "html.parser")
fullContent = []

for shows in content.find_all('li', attrs={"class":"tn-prod-list-item__perf-list-item"}):
    # print(show)
    # print(shows.find(attrs={"class": "tn-prod-list-item__perf-date"}))
    # print(shows.find(attrs={"class": "tn-prod-list-item__perf-time"}))
    showObject = {
        "name": show,
        "date": shows.find(attrs={"class": "tn-prod-list-item__perf-date"}).get_text(),
        "time": shows.find(attrs={"class": "tn-prod-list-item__perf-time"}).get_text()
    }
    fullContent.append(showObject)
    with open('royalExchange.json', 'w') as outfile:
            json.dump(fullContent, outfile)


# for show in shows:
#     print(show.get_Text())

    # showObject = {
    #     "title": show.find('span'),
    #     # "time": show.find(attrs={"class": "tn-prod-list-item__perf-time"}),
    #     # "date": show.find(attrs={"class": "tn-prod-list-item__perf-date"}),
    # }
    # print(showObject)