#Proj6.py
#
# Alexander Powell

from Player import Player

#create player dictionary

# Open the csv file for reading
dataFile = open("passers.csv", "r")
# Create empty dictionary
player_dict = {}

dataFile.readline()
# Iterate through every line in the file and make
# each line a list, split at the commas
for player in dataFile:
    player = player.split(",")
    first = player[0]
    last = player[1]
    name = first + " " + last
    # Add entries to the empty dictionary
    if name in player_dict.keys():
        player_ob = player_dict[name]
        player_ob.update(player[3], player[4], player[6], player[7], player[8], player[9], player[12])
    
    else:
        player_ob = Player(first, last)
        player_dict[name] = player_ob
        player_ob.update(player[3], player[4], player[6], player[7], player[8], player[9], player[12])

# Close the data file
dataFile.close()

key_ring = []

for key in player_dict.keys():
    key_ring.append(key)
    
alpha = []
trigger_count = 0

for key in key_ring:
    player_ob = player_dict[key]
    after_count = 0
    
    if trigger_count == 0:
        alpha.append(player_ob)
        trigger_count = 1
    
    else:
        for other in alpha:
            if player_ob > other:
                after_count += 1
        alpha.insert(after_count, player_ob)
        
for player in alpha:
    print (player)
    
print()

choice = "y"
while choice == "y":
    choice = input("Do you want information about a particular players? ")
    print(choice, "\n")
    choice = choice.lower()

    if choice == "y":
        player_name = input("Enter player's name: ")
        print(player_name, "\n")
        if player_name in player_dict.keys():
            print("Pick one")
            print("a) Overall passer rating")
            print("b) Individual years and ratings \n")
            choice2 = input("Enter choice: ")
            print(choice2,"\n")
            choice2 = choice2.lower()
            if choice2 == "a":
                player_ob = player_dict[player_name]
                print(player_ob, "\n")
            elif choice2 == "b":
                player_ob = player_dict[player_name]
                player_ob.printInfo()
            else:
                print("Error: Invalid entry")
        else:
            print("The player is not in the system. \n")
    
    else:
        print("Thanks for using this program. ")
        print()
