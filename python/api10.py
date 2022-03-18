import json
import requests
try:
    response = requests.get("https://api.covid19api.com/summary")
    data = (response.json())
    for x in data.items():
        print(x)
except:
    print("errir")