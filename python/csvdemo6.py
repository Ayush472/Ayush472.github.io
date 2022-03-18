import csv
reader = csv.reader(open('csv/real_estate.csv', 'r'))
writer = csv.writer(open('csv/copyreal.csv', 'w'))
for row in reader:
    writer.writerow(row)