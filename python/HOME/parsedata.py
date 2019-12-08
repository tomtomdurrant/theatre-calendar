import json 

with open('home.json') as json_data:
    jsonData = json.load(json_data)

for data in jsonData:
    print(data)