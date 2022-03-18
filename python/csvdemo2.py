import csv
with open('csv/real_estate.csv', 'r') as file:
    reader = csv.reader(file,delimiter = '\t')
    for row in reader:
        print(row)