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


        allPlayersArray.append(playerAttributeArray)


print(allPlayersArray)
        # calculate the player value index(points/cost)
        # [6]/[3]





    #




    #     append the new  player importPlayerArray to allPlayersArray
