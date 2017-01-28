# Proj4.py
# CSCI 141
#
# Liam Canty
# lncanty@email.wm.edu
# (757) 751 - 3151
#
# Alexander Powell
# ajpowell@email.wm.edu
# (804) 564 - 6153
#
# File Prologue:
# The NFL is North America's professional men's football league.
# This program finds the best passers in NFL history, determined
# by a formula that computes the passer rating of all the players
# based on their statistics.  The program also outputs other
# statistics which include the player who passed for the most yards
# in a year, the player who passed for the most touchdowns in a year,
# the player who has the highest completions per attemped pass, and
# the player who got the most interceptions.  

#copy is imported to use deepcopy to preserve a master list, more detail in 
#the centeral function.
import copy

def central ():
    '''primary control for the program. This function calls on other functions
    as well as triggiring the player query option. Deepcopy is used to 
    allow one single list to be preserved in the central function and 
    modifiable copies are created to be passed to the functions.'''
    passer_data = open("passers.csv", "r")
    
    alpha_list = info (passer_data)
    
    sort_list = copy.deepcopy(alpha_list)
    bestest = sorter (sort_list)
           
    overall_list = copy.deepcopy(alpha_list)
    total_list = overall (overall_list)
    
    top_list = copy.deepcopy(total_list)
    top_20 (top_list)

    # Pass the main list through all functions
    maxyards = yardage (alpha_list)        
    maxpasstd = passtd (alpha_list)        
    maxcomplete = comp_att (alpha_list)        
    max_yard_att = yard_att (alpha_list)        
    inter = intercept (alpha_list)
            
    choice = ""
    
    while choice != "n":
        choice = input("Are you interested in the overall rating of a player: ")
        print (choice)
        choice.lower()

        # Use if/elif/else statement to lookup overall
        # passer rating for appropriate input.  
        if choice == "y":
            first = input("Enter the player's first name: ")
            print (first,"\n")
            last = input("Enter the player's last name: ")
            print (last,"\n")
            # Pass input to lookup function
            result = lookup (first,last,total_list)
            
        elif choice != 'n':
            print("Please enter 'y' or 'n' to make a choice.\n")
            
        else:
            # Close the file if the user is not interested in
            # the overall rating of a player.  
            passer_data.close()
        

def info (master):
    '''This function takes the data file and discards the first line. It then 
    sorts the players in alphabetical order and returns that list to central'''
    master.seek(0)
    master.readline()
    meta = []
    
    for line in master:
        # Create a list for every line and split each entry of
        # the list based on the commas
        words = line.split(',')
        # Append each list to the new list, meta.  Then sort and return.  
        meta.append(words)
    meta.sort()
                   
    return meta 

def sorter (meta):
    '''This function calculates the passer rating from a number of variables
    and sorts the lists from best rating to worst, but only prints the top
    50 players. '''    
    bestest= []

    # Calculates the passer rating for each individual player
    # and inserts that value in the beginning of the list.  
    for words in meta:
        # Pull out the relevant statistics
        att = int(words[7]) 
        complete = int(words[6]) 
        yards = float(words[11])
        touch = int(words[9]) 
        inter = int(words[12])
        # Solve for the 4 variables in the equation
        c_rate = (((complete/att)*100)-30)/20
        y_rate = (yards - 3) / 4
        t_rate = (touch/att) * 20
        i_rate = 2.375 - ((inter/att)*25)
        rate = ((c_rate + y_rate + t_rate + i_rate) /6) * 100
        words.insert(0,rate)
        del words[6:]
        bestest.append(words)
    # Sort the list from highest to lowest passer rating
    bestest.sort(reverse=True)        
    del bestest[49:]

    # Print output
    print("The top 50 passers based on their passer rating in", end="")
    print("individual years are: \n")
    print("Name                        Year  Rating  Team")
    for player in bestest:
        name = str(player[1]) + " " + str(player[2])        
        print("%-27s %-5s %-7.2f %-15s" % (name, str(player[5]), \
                                          float(player[0]), str(player[4])))
    
    print()


def overall (alpha):
    '''This function takes the alphabetized player list and consolidates a 
    player's information into one entry which is placed into a larger list.
    This list is sorted on overall rating and is returned.'''

    # Initiate empty lists and set lit_count to 0
    old_name = []
    overall = []
    list_count = 0
    
    for player in alpha:
        name = player[0:2]
        
        if name == old_name:
            player_stats = player[5:]
            stat_count = 0
            for stat in player_stats:
                if stat_count != 6 and stat_count != 5:
                    stat_current = int(stat)
                    stat_old = int(old_info[stat_count])
                    stat_combined = stat_current + stat_old
                    old_info[stat_count] = stat_combined
                    stat_count += 1
                else:
                    stat_current = float(stat)
                    stat_old = float(old_info[stat_count])
                    stat_combined = (stat_current + stat_old)/2
                    old_info[stat_count] = stat_combined
                    stat_count += 1                    
            
            
        elif list_count > 0:
            combined_info = base_info + old_info
            att = int(combined_info[7])
            complete = float(combined_info[6])
            yards = float(combined_info[11])
            touch = int(combined_info[9])
            inter = int(combined_info[12])
            c_rate = (((complete/att)*100)-30)/20
            y_rate = (yards - 3) / 4
            t_rate = (touch/att) * 20
            i_rate = 2.375 - ((inter/att)*25)
            rate = (c_rate + y_rate + t_rate + i_rate)/6*100
            combined_info.insert(0,rate)
            del combined_info[6:]
            overall.append(combined_info) 
            
            old_name = player[0:2]
            old_info = player[5:]
            base_info = player[0:5]
            
        else:
            old_name = player[0:2]
            old_info = player[5:]
            base_info = player[0:5]
            list_count = 1
            
    overall.sort(reverse=True)    
    return overall

def top_20 (top):
    '''This function takes the consolidated player list and truncates it to 20
    players. It highlights the top player and then prints the remaining 
    19 players in order of rank.'''
    del top [19:]
    best_player = top.pop(0)
    best_name = str(best_player[1]) + " " + str(best_player[2])
    best_rate = float(best_player[0])
    print ("The best player is: %12s with an overall passer rating of %6.2f.\n"
           % (best_name,best_rate))    
    print ("The remainder of the top 20 are:")    
    rank = 2
    
    for player in top:
        name = str(player[1]) + " " + str(player[2])
        rate = float(player[0])
        print ("%2d   %-20s %-20.2f" % (rank,name,rate))
        rank += 1
    
    print ()

def yardage (players):
    '''This function takes the alphabetized list and selects the player with
    the highest yardage and prints his information.'''

    # Initialize variables to 0
    index_max = 0
    max_yards = 0

    # Iterate through all the players and check to see which
    # player has the highest passing yards value.  Keep track
    # of this by continuously storing the index number of the
    # player you are currently examining.  
    for player in players:
        yards = int(player[8])
        if yards > max_yards:
            index_max = players.index(player)
            max_yards = yards
    # Print output
    bestest = players[index_max]
    player_name = str(bestest[0]) + " " + str(bestest[1])    
    print("The person who passed for the most yardage is: ")
    print("%13s passing %-4i for %-2s in %4s." % (player_name,max_yards,bestest[3],bestest[4]))
    print()
     

def passtd (players):
    '''This function takes the alphabetized list and selects the player with
    the highest count of passing touchdowns and prints his information.'''

    # Initialize variables to 0
    index_max = 0
    max_td = 0

    # Iterate through all the players to check who has the highest
    # passing touchdown count.  
    for player in players:
        td = int(player[9])
        if td > max_td:
            index_max = players.index(player)
            max_td = td

    # Print Output
    bestest = players[index_max]
    player_name = str(bestest[0]) + " " + str(bestest[1])    
    print("The person who scored the most passing touchdowns is:")
    print("%12s scoring %2i touchdowns for %-2s in %4s." % (player_name,max_td,bestest[3],bestest[4]))
    print()
    

def comp_att (players):
    '''This function takes the alphabetized list and selects the player with
    the highest completions per attempt and prints his information.'''

    # Initialize variables to 0
    index_max = 0
    max_comp = 0

    # Iterate through all the players to see who has the
    # greatest ratio of completions to attempts
    for player in players:
        comp = int(player[6])
        att = int(player[7])
        comp_att = (comp/att) * 100
        if comp_att > max_comp:
            index_max = players.index(player)
            max_comp = comp_att

    # Print Output
    bestest = players[index_max]
    player_name = str(bestest[0]) + " " + str(bestest[1])    
    print("The person who has the highest completions per attempted pass is:")
    print("%13s with a %-4.2f percent completion rate for %-3s in %4s." % (player_name,max_comp,bestest[3],bestest[4]))
    print()

def yard_att (players):
    '''This function takes the alphabetized list and selects the player with
    the highest yards per attempt and prints his information.'''

    # Initialize variables to 0
    index_max = 0 
    max_yard = 0 

    # Iterate through all the players to check which one
    # has the greatest ratio of yards to attempt.  
    for player in players:
        yard = int(player[8])
        att = int(player[7])
        yard_att = yard/att
        if yard_att > max_yard:
            index_max = players.index(player)
            max_yard = yard_att

    # Print output
    bestest = players[index_max]
    percent_yard = max_yard*100
    player_name = str(bestest[0]) + " " + str(bestest[1])    
    print("The person who passed for the most yardage is: ")
    print("%14s with %-4.1f yards per attempt for %-3s in %4s." % (player_name,max_yard,bestest[3],bestest[4]))
    print()
    

def intercept (players):
    '''This function takes the alphabetized list and selects the player with
    the highest number of interceptions and prints his information.'''

    # Initialize variables to 0
    index_max = 0
    max_inter = 0

    # Iterate through all the players to see who has
    # the most interceptions.  
    for player in players:
        inter = int(player[12])
        if inter > max_inter:
            index_max = players.index(player)
            max_inter = inter

    # Print output
    bestest = players[index_max]
    player_name = str(bestest[0]) + " " + str(bestest[1])    
    print("The person with the most interceptions in a season is:")
    print("%16s with %-2i interceptions for %-3s in %4s." % (player_name,max_inter,bestest[3],bestest[4]))
    print()
       
            
def lookup (first,last,lookup):
    '''This function takes the consilidated list and finds the overall rating
    of a player defined by user input.'''

    # Assign input statements to variables, then join them together
    new_first = first.lower()
    new_last = last.lower()
    query = new_first + " " + new_last

    # Look through the list to find the player with the same name
    for player in lookup:
        player_name = str(player[1]) + " " + str(player[2])
        lowercase = player_name.lower()
        player_rate = float(player[0])
        # Print results
        if query == lowercase:
            print ("%-16s %-5.2f" % (player_name,player_rate))
            print()

central()
