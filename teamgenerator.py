import csv



# create a blank array named allPlayersArray
allPlayersArray =[]




# import the csv file
with open('nfl.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    # for each line in csv file
        # initialize counter
    count = 0
    for line in csv_reader:
        count +=1
    #     create new importPlayerArray for the line
        importPlayerArray = []

    #     add player "id number" to importPlayerArray in the position 0 in the array

    #         "id number" = the number of itterations in the for loop 1
    #
    #     determine if the player is offensie or defensive
    #      if the positon is offensive then lable it offensive
    #         offiensive positions are ["qb", "rb", "fb", "wr", "te", "lt", "lg", "c", "rg", "rt", "k", "r", "pr"]
    #         deffensive positions are ["de", "dt", "lb", "olb", "ilb", "mlb", "cb", "s"]
    #         add offensive/defensive value to importPlayerArray to position 1 in the array
    #
    #     calculate the player value index(points/cost)
    #
    #     append the new  player importPlayerArray to allPlayersArray
