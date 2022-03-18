import csv
reader = csv.reader(open('csv/real_estate.csv', 'r'))
writer = csv.writer(open('csv/copyrealrich.csv', 'w'))
c=0
for row in reader:
    if row[7]=='Condo':
        writer.writerow(row)
        c=c+1
print("Total ",c)

