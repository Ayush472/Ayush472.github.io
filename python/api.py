
import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.status_code)
except:
    print("errir")