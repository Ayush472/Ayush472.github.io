import requests
import json
try:
    response = requests.get("https://official-jokeapi.appspot.com/random_joke")
    obj = (response.json())
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
except:
    print("errir")
