import csv
with open('csv/real_estate.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1]," -- ", row[7]," -- ",row[9])