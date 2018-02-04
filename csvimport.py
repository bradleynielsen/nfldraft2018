import csv
allPlayersArray = []

with open('nfl.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)


    for line in csv_reader:
        # print(line)
        allPlayersArray.append(line)



# for n in range(len(allPlayersArray[])):
#     print(allPlayersArray[n])
#     print(allPlayersArray[n+1])

n=0
print(allPlayersArray[n])
print(allPlayersArray[n+1])


# print(allPlayersArray[3:])
