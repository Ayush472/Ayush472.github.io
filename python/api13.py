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
print(list1)
print(list2)


pos1 = list2.index(max(list2))
pos2 = list2.index(min(list2))
print("Heighst Cases in Country ", list1[pos1], " Cases ", max(list2))
print("Lowest Cases in Country ", list1[pos2], " Cases ", min(list2))