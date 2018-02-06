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
    index1 = totalLength - remainderLength+1

    # print(totalLength)
    # print(remainderLength)

    for n in range(len(defensivePlayersArray[i:])):
        # initialize new group
        newDefenseGroup = []
        # print(i)
        # print(index1)


        if i < index1:
            try:
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
            except:
                continue
        else:
            continue
# for i in range(len(defenseGroupsArray)):
#     print(defenseGroupsArray[i])
# totalDefenseCombinations = len(defenseGroupsArray)
# print(" total defense combinations: " + repr(totalDefenseCombinations))



##############################################################################
# OFFENSE GROUP GENERATION
##############################################################################

# init the array
offenseGroupsArray = []
# loop1 itterates over the offense players array,
# creating the value for index 0 of the newOffenseGroup
for l1 in range(len(offensivePlayersArray)):
    index0 = l1
    index1 = index0+1
    offenseTotalLength = len(offensivePlayersArray)
    # print(offenseTotalLength)
    # print(loop1RemainderLength)
    # print(index0)
    # print(index1)
    # print(index2)
    # print(index3)

    # loop2
    for l2 in range(len(offensivePlayersArray[index1:])):
        index2 = index1+1
        # loop3
        for l3 in range(len(offensivePlayersArray[index2:])):
            index3 = index2+1
            # loop4
            for l4 in range(len(offensivePlayersArray[index3:])):
                # print("index 0: " + repr(index0) + " index 1: " + repr(index1) + " index 2: " + repr(index2) + " index 3: " + repr(index3))
                # init new groupPoints
                newOffenseGroupArray = []
                # append players to new array
                newOffenseGroupArray.append(offensivePlayersArray[index0])
                newOffenseGroupArray.append(offensivePlayersArray[index1])
                newOffenseGroupArray.append(offensivePlayersArray[index2])
                newOffenseGroupArray.append(offensivePlayersArray[index3])

                # calculate group cost
                index0Cost = float(offensivePlayersArray[index0][1])
                index1Cost = float(offensivePlayersArray[index1][1])
                index2Cost = float(offensivePlayersArray[index2][1])
                index3Cost = float(offensivePlayersArray[index3][1])
                groupCost = index0Cost+index1Cost+index2Cost+index3Cost

                # append the cost to the group
                newOffenseGroupArray.append(groupCost)

                # calculate group points
                index0Points = float(offensivePlayersArray[index0][5])
                index1Points = float(offensivePlayersArray[index1][5])
                index2Points = float(offensivePlayersArray[index2][5])
                index3Points = float(offensivePlayersArray[index3][5])

                groupPoints = index0Points+index1Points+index2Points+index3Points
                # print(groupPoints)

                # append the cost to the group
                newOffenseGroupArray.append(groupPoints)

                # append new group to array
                offenseGroupsArray.append(newOffenseGroupArray)

                index3 +=1
            # end loop4
            index2 +=1
        # end loop3
        index1 +=1
    # end loop2
# end loop1

# for i in range(len(offenseGroupsArray)):
#     print(offenseGroupsArray[i])
# totalOffenseCombinations = len(offenseGroupsArray)
# print(" total Offense combinations: " + repr(totalOffenseCombinations))




########################################################################
# Create teams

allTeamsArray = []
teamNumber = 1
for o in range(len(offenseGroupsArray)):
    for d in range(len(defenseGroupsArray)):
        newTeamArray = []
        newTeamArray.append(teamNumber)
        teamNumber +=1

        # append each of the offense players
        for i in range(4):
            newTeamArray.append(offenseGroupsArray[o][i])

        # append each of the defense players
        for i in range(2):
            newTeamArray.append(defenseGroupsArray[d][i])

        # calculate the cost offense + defense
        offenseCost = offenseGroupsArray[o][4]
        defenseCost = defenseGroupsArray[d][2]
        teamCost = offenseCost+defenseCost

        # calculate the points offense + defense
        offensePoints = offenseGroupsArray[o][5]
        defensePoints = defenseGroupsArray[d][3]
        teamPoints = offensePoints + defensePoints

        # append the cost
        newTeamArray.append(teamCost)
        newTeamArray.append(teamPoints)

        # print("Adding team #" + str(teamNumber))

        # append the new team to the all teams array
        if teamCost <= 50000 and teamCost > 49950 and teamPoints > 109:
            allTeamsArray.append(newTeamArray)
            print(newTeamArray)
        else:
            continue

totalTeams = len(allTeamsArray)
print(totalTeams)

# # write the results to csv_file
#
# csvfile = "results.csv"
# with open(csvfile, "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerows[totalTeams]
