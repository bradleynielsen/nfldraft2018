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

        #append the new  player importPlayerArray to allPlayersArray
        allPlayersArray.append(playerAttributeArray)

# print all players
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

##############################################
# player type reader
# print("these are the offensive players")
# for iii in range(len(offensivePlayersArray)):
#     print(offensivePlayersArray[iii])
# print("these are the defensive players")
# for iii in range(len(defensivePlayersArray)):
#     print(defensivePlayersArray[iii])

# for iii in range(len(defensivePlayersArray)):
#     print(defensivePlayersArray[i])
##############################################


##############################################################################
# DEFENSE GROUP GENERATION
##############################################################################
# Generate all defense combinations

# init the array
defenseGroupsArrCay = []

# loop over the players array
for i in range(len(defensivePlayersArray)):
    # create a group with the pivot and the  thest of the arrays
    totalLength = len(defensivePlayersArray)
    remainderLength = len(defensivePlayersArray[i:])
    index1 = totalLength - remainderLength
    # print(index1)
    for n in range(len(defensivePlayersArray[i:])):
        # create the position index for the second slot
        # this creates a place holder for each unique combination of players
        # initialize new group
        newDefenseGroup = []

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
offenseGroupsArrCay = []
for i in range(len(offensivePlayersArray)):
