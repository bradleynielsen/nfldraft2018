import csv
nflArray = []

with open('nfl.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        # print(line)
        nflArray.append(line)



for s in nflArray:
    print(s) 
