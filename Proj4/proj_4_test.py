import csv
import copy
dataFile = open("passers_copy.csv", "r")
nfl_list = []
rating_list = []
line = dataFile.readline()
for line in dataFile:
    line = line.lower()
    line_list = line.split(",")
    nfl_list.append(line_list)
    c_var = ((((int(line_list[6]))/(int(line_list[7]))) * 100)-30) / 20
    y_var = ((float(line_list[11])) - 3) / 4
    t_var = ((int(line_list[9]))/(int(line_list[7]))) * 20
    i_var = 2.375 - (((int(line_list[12])) / (int(line_list[7]))) * 25)
    pass_rating = ((c_var + y_var + t_var + i_var) / 6) * 100
    print(line_list, "line list")
    #print(line_list[0], line_list[1], " had a passer rating of ", pass_rating)
#    rating_list.append(pass_rating and line_list[0] and line_list[1])
#print(rating_list)
line_list2 = line_list
#line_list2.insert(pass_rating)
count = 0
nfl_list.sort()
print(nfl_list, "nfl list")
print(nfl_list[0])
    



choice = ''
lookup_list = copy.deepcopy(nfl_list)
while choice != 'n':
    choice = input("Are you interested in the overall rating of a player: ")
    print (choice)
    choice.lower()
    if choice == 'y':
        first = input("Enter the player's first name: ")
        print (first)
        last = input("Enter the player's last name: ")
        print (last)
        #result = lookup (first,last,lookup_list)
        for player in line_list:
            if first == line_list[0] and last == line_list[1]:
                print(first, last)
    else:
        print("Invalid entry.  Try again. ")

    

#question = input("Are you interested in the overall rating of a particular player? ")
#print(question)
#if question == "y":
#    first_name = input("Enter the player's first name: ")
#    print(first_name)
#    last_name = input("Enter the player's last name: ")
#    print(last_name)
#    #if first_name == ### and last_name == ###


dataFile.close()
