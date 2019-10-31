import csv

with open('D:\Others\Data\school.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
    print(row[0])


