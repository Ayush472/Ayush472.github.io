import requests
import json
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    obj=(response.json())
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
except:
    print("errir")