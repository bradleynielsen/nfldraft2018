import csv



# create a blank array named allPlayersArray
# to convert .csv to a 2 dementional array of players w/ attributes
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

        # add player w/ attributes to the playerAttributeArray
        for i in range(len(line)):
            playerAttributeArray.append(line[i])

        #determine if the player is offensie or defensive
        #offiensive positions are:
        # ["qb", "rb", "fb", "wr", "te", "lt", "lg", "c", "rg", "rt", "k", "r", "pr"]
        #deffensive positions are:
        # ["de", "dt", "lb", "olb", "ilb", "mlb", "cb", "s"]
        playerPosition = playerAttributeArray[1]
        if playerPosition in offenseArray:
            playerType = 'offense'
        elif playerPosition in defenseArray:
            playerType = 'defense'

        #add offensive/defensive value to importPlayerArray to the array
        playerAttributeArray.append(playerType)
        # print("the current player is ")
        # print(playerAttributeArray[2])
        # print(playerAttributeArray)

        # calculate the player value index(points/cost)
        playerAvgPoints = float(playerAttributeArray[5])
        playerCost = float(playerAttributeArray[3])
        playerValueIndex = playerAvgPoints/playerCost
        # print(playerValueIndex)
        playerAttributeArray.append(playerValueIndex)

        #append the new  player importPlayerArray to allPlayersArray
        allPlayersArray.append(playerAttributeArray)

# # print all players
# for n in range(len(allPlayersArray)):
#     print(allPlayersArray[n])

# initialize arrays for plyaer type groups
offensivePlayersArray = []
defensivePlayersArray = []

# create offensive  players  array
offenseCount = 0
defenseCount = 0
for ii in range(len(allPlayersArray)):
    if allPlayersArray[ii][7] == 'offense':
        newOffensivePlayer = []
        # 0 player GUID
        newOffensivePlayer.append(allPlayersArray[ii][0])
        # 1 cost
        newOffensivePlayer.append(allPlayersArray[ii][3])
        # 2 name
        newOffensivePlayer.append(allPlayersArray[ii][2])
        # 3 group UID
        newOffensivePlayer.append(allPlayersArray[ii][8])
        # 4 points
        newOffensivePlayer.append(allPlayersArray[ii][5])

        offenseCount +=1
        newOffensivePlayer.append(offenseCount)
        offensivePlayersArray.append(newOffensivePlayer)

    # or create defensensive players array
    elif allPlayersArray[ii][7] == 'defense':
        newDefensivePlayer = []
        # 0 player GUID
        newDefensivePlayer.append(allPlayersArray[ii][0])
        # 1 cost
        newDefensivePlayer.append(allPlayersArray[ii][3])
        # 2 name
        newDefensivePlayer.append(allPlayersArray[ii][2])
        # 3 group UID
        newDefensivePlayer.append(allPlayersArray[ii][8])
        # 4 points
        newDefensivePlayer.append(allPlayersArray[ii][5])

        defenseCount +=1
        newDefensivePlayer.append(defenseCount)
        defensivePlayersArray.append(newDefensivePlayer)

##############################################################################
# player type reader
# print("these are the offensive players")
# for i in range(len(offensivePlayersArray)):
#     print(offensivePlayersArray[i])
# print("these are the defensive players")
# for i in range(len(defensivePlayersArray)):
#     print(defensivePlayersArray[i])

# for i in range(len(defensivePlayersArray)):
#     print(defensivePlayersArray[i])
##############################################################################


##############################################################################
# DEFENSE GROUP GENERATION
##############################################################################
# Generate all defense combinations

# init the array
defenseGroupsArray = []

# loop over the players array
for i in range(len(defensivePlayersArray)):
    # create a group with the pivot and the  thest of the arrays
    totalLength = len(defensivePlayersArray)
    remainderLength = len(defensivePlayersArray[i:])
    # create the position index for the second slot
    index1 = totalLength - remainderLength

    # print(totalLength)

    for n in range(len(defensivePlayersArray[i:])):
        # initialize new group
        newDefenseGroup = []
        print(i)
        print(index1)

        # append the pivot player to index 0 of the newDefenseGroup array
        newDefenseGroup.append(defensivePlayersArray[i])

        # append the next player to index 1 of the newDefenseGroup array
        newDefenseGroup.append(defensivePlayersArray[index1])

        # calculate group cost
        index0Cost = float(defensivePlayersArray[i][1])
        index1Cost = float(defensivePlayersArray[index1][1])
        groupCost = index0Cost+index1Cost

        # append the cost to the group
        newDefenseGroup.append(groupCost)

        # calculate group points
        index0Points = float(defensivePlayersArray[i][5])
        index1Points = float(defensivePlayersArray[index1][5])

        groupPoints = index0Points+index1Points
        # print(groupPoints)

        # append the cost to the group
        newDefenseGroup.append(groupPoints)
        # advance the index1
        index1 +=1

        # newDefenseGroup.append(defensivePlayersArray[index1])
        # print(newDefenseGroup)
        defenseGroupsArray.append(newDefenseGroup)

# for i in range(len(defenseGroupsArray)):
#     print(defenseGroupsArray[i])
# print(len(defenseGroupsArray))



##############################################################################
# OFFENSE GROUP GENERATION
##############################################################################
offenseGroupsArray = []
# first for loop itterates over the offense players array,
# creating the value for index 0 of the newOffenseGroup
for index0Counter in range(len(offensivePlayersArray)):
    totalLength = len(offensivePlayersArray)
    loop1RemainderLength = len(offensivePlayersArray[index0Counter:])
    index0 = index0Counter
    index1 = totalLength - loop1RemainderLength
    # print("index 0: " + repr(index0))
    # print("index 1: " + repr(index1))

    # second for loop itterates over the offense players array,
    # creating the value for index 1 of the newOffenseGroup
    # for index1Counter in range(len(offensivePlayersArray[index0Counter]:))
            # index2 = totalLength -
