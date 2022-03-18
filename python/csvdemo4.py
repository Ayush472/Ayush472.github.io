import csv
csv.register_dialect('myDialect',skipinitialspace=True,quoting=csv.QUOTE_ALL)
with open('csv/real_estate.csv', 'r') as file:
    reader = csv.reader(file, dialect='myDialect')
    for row in reader:
        print(row)
        