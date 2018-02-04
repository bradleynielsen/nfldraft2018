import csv



# create a blank array named allPlayersArray
allPlayersArray =[]
defenseArray = ["DE", "DT", "LB", "OLB", "ILB", "MLB", "CB", "S"]
offenseArray = ["QB", "RB", "FB", "WR", "TE", "LT", "LG", "C", "RG", "RT", "K", "R", "PR"]




# import the csv file
with open('nfl.csv', 'r') as csv_file:
    # set variable based on the imported csv method
    csv_reader = csv.reader(csv_file)

    # initialize counter
    count = 0

    # for each line in csv file add a player to the player array
    for line in csv_reader:
        # itterate the counter
        count +=1

        #create new importPlayerArray for the line and add the player
        playerAttributeArray = []

        #add player "id number" to importPlayerArray in the position 0 in the array
        playerID = count
        playerAttributeArray.append(playerID)

        # add player information to the playerAttributeArray
        for i in range(len(line)):
            playerAttributeArray.append(line[i])

        # playerAttributeArray.append()

        ######################################################################
        #determine if the player is offensie or defensive
        #offiensive positions are ["qb", "rb", "fb", "wr", "te", "lt", "lg", "c", "rg", "rt", "k", "r", "pr"]
        #deffensive positions are ["de", "dt", "lb", "olb", "ilb", "mlb", "cb", "s"]
        playerPosition = playerAttributeArray[1]



        if playerPosition in offenseArray:
            playerType = 'offense'
        elif playerPosition in defenseArray:
            playerType = 'defense'

        #add offensive/defensive value to importPlayerArray to position n in the array
        playerAttributeArray.append(playerType)
        # print("the current player is ")
        # print(playerAttributeArray[2])
        # print(playerAttributeArray)

        # calculate the player value index(points/cost)
        # [6]/[3]
        playerAvgPoints = float(playerAttributeArray[5])
        playerCost = float(playerAttributeArray[3])
        playerValueIndex = playerAvgPoints/playerCost
        # print(playerValueIndex)
        playerAttributeArray.append(playerValueIndex)

        allPlayersArray.append(playerAttributeArray)

#append the new  player importPlayerArray to allPlayersArray
# print(allPlayersArray)

# initialize arrays for plyaer type groups
offensivePlayersArray = []
defensivePlayersArray = []

# create offensive  players  array
for ii in range(len(allPlayersArray)):
    if allPlayersArray[ii][7] == 'offense':
        newOffensivePlayer = []
        newOffensivePlayer.append(allPlayersArray[ii][0])
        newOffensivePlayer.append(allPlayersArray[ii][3])
        newOffensivePlayer.append(allPlayersArray[ii][2])
        newOffensivePlayer.append(allPlayersArray[ii][8])
        offensivePlayersArray.append(newOffensivePlayer)
    # or create defensensive players array
    elif allPlayersArray[ii][7] == 'defense':
        newDefensivePlayer = []
        newDefensivePlayer.append(allPlayersArray[ii][0])
        newDefensivePlayer.append(allPlayersArray[ii][3])
        newDefensivePlayer.append(allPlayersArray[ii][2])
        newDefensivePlayer.append(allPlayersArray[ii][8])
        defensivePlayersArray.append(newDefensivePlayer)


print("these are the offensive players")
print(offensivePlayersArray)

print("these are the defensive players")
print(defensivePlayersArray)

# select the defense group
for iii in range(len(defensivePlayersArray)):
    # set iii number plyer to base
    basePlayer = defensivePlayersArray[iii]
