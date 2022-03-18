import requests
import json
try:
    response = requests.get("https://api.covid19api.com/summary")
    obj = (response.json())
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
except:
    print("errir")
