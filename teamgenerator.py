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
        print("the current player")
        print(playerAttributeArray)

        ######################################################################
        #determine if the player is offensie or defensive
        #offiensive positions are ["qb", "rb", "fb", "wr", "te", "lt", "lg", "c", "rg", "rt", "k", "r", "pr"]
        #deffensive positions are ["de", "dt", "lb", "olb", "ilb", "mlb", "cb", "s"]
        playerPosition = playerAttributeArray[1]
        print(playerPosition)

        if playerPosition in offenseArray:
            playerType = 'offense'
        elif playerPosition in defenseArray:
            playerType = 'defense'

        print(playerType)











        # if offenseArray.index(playerPosition) >= 0:
        #     playerType = 'deffense'
        #     defense = False
        # elif defenseArray.index(playerPosition) >= 0:
        #     playerType = 'offense'
        #     offense = False
        # # if defenseArray.index(playerPosition) >= 0:
        # #     playerType = 'offense'
        # #     offense = False
        # # elif offenseArray.index(playerPosition) >= 0:
        # #     playerType = 'deffense'
        # #     defense = False





        #add offensive/defensive value to importPlayerArray to position n in the array




    #     calculate the player value index(points/cost)
    #
    #     append the new  player importPlayerArray to allPlayersArray
