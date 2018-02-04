import csv
allPlayersArray = []

with open('nfl.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)


    for line in csv_reader:
        # print(line)
        allPlayersArray.append(line)



# for n in allPlayersArray:
    # print(n)
    # print(line[n])


print(allPlayersArray[3][3])
