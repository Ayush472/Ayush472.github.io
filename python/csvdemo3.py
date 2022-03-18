import csv
with open('csv/real_estate.csv', 'r') as file:
    reader = csv.reader(file,skipinitialspace=True)
    for row in reader:
        print(row)