import json
try:
    with open('jsonfiles/1.json') as file_object:
        data = json.load(file_object)
        print(type(data))
except:
    print("errir")