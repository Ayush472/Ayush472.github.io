import json
try:
    with open('jsonfiles/students.json') as file_object:
        data = json.load(file_object)
        for x in data['Student']:
            print(x['Name'])
except:
    print("errir") 