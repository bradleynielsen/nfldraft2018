#######################################################################
# loop3
for loop3Counter in range(len(offensivePlayersArray[loop2Counter:])):
    #######################################################################
    # loop4
    for index3Counter in range(len(offensivePlayersArray[index2:])):
        # adds the resulting index value to the new group array
        # and apends that to the offense team array
        # print("Index 0: " + repr(index0) + " Index 1: " + repr(index1) + " Index 2: " + repr(index2) + " Index 3: " + repr(index3))
        index3 +=1
    # end loop4
    #######################################################################
    index2 +=1
    # print("index 0: " + repr(index0) + " index 1: " + repr(index1) + " index 2: " + repr(index2))


# end loop3
#######################################################################



# loop2
for l2 in range(len(offensivePlayersArray[l1:])):
    if index0 < index1 < index2 < index3:
        # loop3
        for l3 in range(len(offensivePlayersArray[l2:])):
            if index0 < index1 < index2 < index3:
                index2 +=1
                # loop4
                for l4 in range(len(offensivePlayersArray[l3:])):
                    if index0 < index1 < index2 < index3:
                        print("index 0: " + repr(index0) + " index 1: " + repr(index1) + " index 2: " + repr(index2))
                        index3 +=1
                    else:
                        continue
                # end loop4

            else:
                continue
        # end loop3
    else:
        continue
    index1 +=1
# end loop2
