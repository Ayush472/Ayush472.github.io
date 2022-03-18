import requests
try:
    response =requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.json())
except:
    print("errir")