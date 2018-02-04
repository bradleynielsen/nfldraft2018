import csv



# create a blank array named allPlayersArray
allPlayersArray =[]




# import the csv file
with open('nfl.csv', 'r') as csv_file:
    # set variable based on the imported csv method
    csv_reader = csv.reader(csv_file)

    # initialize counter
    count = 0

    # for each line in csv file
    for line in csv_reader:
        # itterate the counter
        count +=1

        #create new importPlayerArray for the line and add the player
        newPlayerArray = []

        #add player "id number" to importPlayerArray in the position 0 in the array
        playerID = counter
        newPlayerArray.append(playerID)

        # add player information to the newPlayerArray
        newPlayerArray.append(line)

        ######################################################################
        #determine if the player is offensie or defensive
        #offiensive positions are ["qb", "rb", "fb", "wr", "te", "lt", "lg", "c", "rg", "rt", "k", "r", "pr"]
        #deffensive positions are ["de", "dt", "lb", "olb", "ilb", "mlb", "cb", "s"]



        #add offensive/defensive value to importPlayerArray to position 1 in the array

    #     calculate the player value index(points/cost)
    #
    #     append the new  player importPlayerArray to allPlayersArray
