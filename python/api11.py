import json
import requests
try:
    response = requests.get("https://api.covid19api.com/summary")
    data = (response.json())
    for x in data['Countries']:
        print(x['Country'], " | ", x["NewConfirmed"])
except:
    print("errir")