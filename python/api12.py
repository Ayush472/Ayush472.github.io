import json
import requests
list1=[]
list2=[]
response = requests.get("https://api.covid19api.com/summary")
data = (response.json())
for x in data['Countries']:
    if x["NewConfirmed"]>0:
        list1.append(x['Country'])
        list2.append(x["NewConfirmed"])