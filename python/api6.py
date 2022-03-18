import json
try:
    with open('jsonfiles/students1.json') as file_object:
        data = json.load(file_object)
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)
except:
    print("errir")