import json 

with open('royalExchange.json') as json_data:
    jsonData = json.load(json_data)

for data in jsonData:
    print(data["date"] + " " + data["time"]) 