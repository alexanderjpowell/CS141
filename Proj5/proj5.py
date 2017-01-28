# Proj5.py
# 
# CSCI 141
# 
# 11/18/2013
# 
# Alexander Powell, ajpowell@email.wm.edu, (804) 564 - 6153
#
# Liam Canty, Lncanty@email.wm.edu, (757) 757-3151.
# 
# 
# Prologue: This program read information from a csv file which contains
# information about hundreds of football players in the NFL.
# The user is faced with three choices; a) they can
# look up information about any particular player in the file, including
# the teams they've played for and what years they played for those teams,
# as well as their individial passer ratings for every year they've
# competed in the NFL, as well as their overall passer rating, b) they
# can look up information about any team in the file, including which
# players have played for that team and in what years, as well as those
# players' passer rating, and c) they can see a list of every player
# in the csv file, sorted in alphabetical order by last name, with
# that player's passer rating.  


def info (players):
    '''Sorts the list of players in alphabetical order and stores
all the information in lists. '''

    players.readline()
    all_players = []

    # Iterate through all the lines in the csv file and create
    # a list for every player, separating every element in the
    # list based on the commas in the csv.  
    for line in players:
        words = line.split(",")
        all_players.append(words)
    all_players.sort()

    return all_players


def passer_rating (players):
    '''Calculate the passer rating for each player.  '''

    best_players = []

    # Calculate the passer rating for every player
    # by indexing the lists created in the info function above
    for player in players:
        att = int(player[7])
        complete = int(player[6])
        yards = int(player[8])/int(player[7])
        touch = int(player[9])
        inter = int(player[12])
        comp_rate = (((complete/att) * 100) - 30) / 20
        yard_rate = (yards - 3) / 4
        td_rate = (touch/att) * 20
        inter_rate = 2.375 - ((inter/att) * 25)
        rate = (comp_rate + yard_rate + td_rate + inter_rate) / 6 * 100
        player.insert(0,rate)
        best_players.append(player)

    # Sort the lists based on who has the best passer rating
    best_players.sort()
    
    return best_players


def player_dict_func (players):
    '''Returns a dictionary with the player's name as the key
and the player's info (like his year, team, and passer rating)
stored in a tuple as the value. '''

    # Create an empty dictionary
    player_dict = {}

    # Iterate though each individial list and add the
    # relevent items to the empty dictionary
    for player in players:
        team = city_conversion[player[4]]
        first = player[1]
        last = player[2]
        name = first + " " + last
        player_info = player[5], team, player[0]
        # If the player's name already has an entry in the
        # dictionary, append his player info to the end of the list
        if name in player_dict.keys():
            info = player_dict[name]
            info.append(player_info)
            player_dict[name] = info            
        else:
            player_list = [player_info]
            player_dict[name] = player_list

    # Return the final dictionary
    return player_dict


def team_dict_func (players):
    '''Returns a dictionary with the team as the key and a tuple
which includes the year, name, and rating of every player
as the value. '''

    # Create an empty dictionary
    my_dict = {}

    # Iterate though each individial list and add the
    # relevent items to the empty dictionary
    for player in players:
        team = city_conversion[player[4]]
        first = player[1]
        last = player[2]
        name = first + " " + last
        player_info = player[5], name, player[0]
        # If the team already has an entry in the
        # dictionary, append the player info to the end of the list
        if team in my_dict.keys():
            info = my_dict[team]
            info.append(player_info)
            my_dict[team] = info            
        else:
            player_list = [player_info]
            my_dict[team] = player_list

    # Return the final dictionary
    return my_dict


def overall (alpha):
    '''This function takes the alphabetized player list and consolidates a 
    player's information into one entry which is placed into a larger list.
    This list is sorted on overall rating and is returned.'''
    
    # Initiate empty lists and set lit_count to 0  
    old_name = ''
    total_dict = {}
    list_count = 0
    
    
    for player in alpha:
        name = player[0:2]
        
        
        #If the player name is the same of the last name, add up his statistics
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
            
        #if the player name is not equal to the previous player's name (execpt 
        #for the first player name) a rating is calculated. old and base info 
        #are then set to the current player.
        elif list_count > 0:
            combined_info = base_info + old_info
            att = int(combined_info[7])
            complete = int(combined_info[6])
            yards = int(combined_info[8])/int(combined_info[7])
            touch = int(combined_info[9])
            inter = int(combined_info[12])
            comp_rate = (((complete/att) * 100) - 30) / 20
            yard_rate = (yards - 3) / 4
            td_rate = (touch/att) * 20
            inter_rate = 2.375 - ((inter/att)*25)
            rate = (comp_rate + yard_rate + td_rate + inter_rate) / 6 * 100
            total_dict[player_name] = rate            
            
            old_name = player[0:2]
            old_info = player[5:]
            base_info = player[0:5]
            player_name = str(player[1]) + ", " + str(player[0])
        
        #for the first and only the first player entry set up old and base 
        #information without triggering a calculation of rating
        else:
            old_name = player[0:2]
            old_info = player[5:]
            base_info = player[0:5]
            list_count = 1
            player_name = str(player[1]) + ", " + str(player[0])
            
    return total_dict


def all_players (total_dict):
    '''Prints the list of players in a neatly formatted manner.'''
    
    key_ring = [] 
    
    for key in total_dict.keys():
        key_ring.append(key)
            
    key_ring.sort()
    
    for key in key_ring:
        print ("%-23s %5.2f" % (key, total_dict[key]))
    


import copy

# Establish the dictionary which includes the teams' abbreviations as
# key and their full names as dictionary values.
city_conversion = {'MIA': 'Miami', 'NO':'New Orleans', 'STL':'St. Louis',\
'NE':'New England','SD':'San Diego','HOU':'Houston','MIN':'Minnesota',\
'IND':'Indianapolis','TEN':'Tennessee','OAK':'Oakland','ARI':'Arizona',\
'KC':'Kansas City','SF':'San Francisco','GB':'Green Bay','DAL':'Dallas',\
'DET':'Detroit','BAL':'Baltimore','CLE':'Cleveland','CIN':'Cincinnati',\
'WAS':'Washington','DEN':'Denver','NYG':'New York Giants',\
'NYJ':'New York Jets','SEA':'Seattle','ATL':'Atlanta', 'CAR':'Carolina',\
'PHI':'Philadelphia','BUF':'Buffalo','CHI':'Chicago','TB':'Tampa Bay',\
'PIT':'Pittsburgh','JAX':'Jacksonville','BOS':'Boston',\
'BCL': 'Baltimore Colts','NYY': 'New York Yankees','NYT': 'Newark Tornadoes',\
'DTX':'Dallas Texans','RAM': 'Los Angeles Rams','RAI':'Oakland Raiders',\
'LAD':'Los Angeles Dons','LAC':'Los Angeles Chargers','CRD':'Chicago Cardinals'}

# Open the data file for reading
dataFile = open("passers_new.csv", "r")

alpha_list = info(dataFile)

# Print the user input menu
choice = ''
while choice != "q":
    print("Menu Choices ")
    print("a) Find a passer and print his career information and overall rating.")
    print("b) Find a team and print all the passers by year. ")
    print("c) Print a list of players and their ratings in alpha order. ")
    print("q) Quit ")
    print()

    choice = input("Enter choice: ")
    print(choice)
    print()
    choice = choice.lower()

    # Use an if/elif/else statement to direct user input to
    # relevent functions in the code
    if choice == "a":
        first_last = []
        name = input("Enter the player's full name: ")
        print(name)
        print()
        first_last = name.split(" ", 1)
        name_overall = first_last[1] + ", " + first_last[0]
        
        over_list = copy.deepcopy(alpha_list)
        overall_person = overall (over_list)
        individual_list = copy.deepcopy(alpha_list)
        player_dict_list = passer_rating (individual_list)
        individuals = player_dict_func (player_dict_list) 
        
        if name in individuals:
            response = individuals[name]
            response.sort()
            print (name)
            for year in response:
                print ("    played for",year[1], "in", year[0], 
                       "with a rating of", end= "")
                print (" %5.2f" % (year[2]))     
            print (name, "has an overall rating of", end = "")
            print ((" %5.2f" % (overall_person[name_overall])))
            print()
                
        # Include an else statement for cases when the user
        # enters a name that doesn't exist in the file
        else:
            print("This person is not in the database. ")
            print()

    elif choice == "b":
        team_input = input("Enter the team's initials: ")
        print(team_input)
        team = team_input.upper()
        if team in city_conversion:
            team = city_conversion[team]
            print()
        
            pass_list = copy.deepcopy(alpha_list)
            pass_rating = passer_rating (pass_list)
            team_dict = team_dict_func (pass_rating)        
        
            print(team)
            team_players = team_dict[team]
            team_players.sort()
            for person in team_players:
                print ("    ",person[1], "played in", person[0], 
                       "with a rating of", end= "")
                print (" %5.2f" % (person[2])) 
            print ()

        # Include an else statement for cases when the user
        # enters a name that doesn't exist in the file
        else:
            print()
            print("This team is not in the database. ")
            print()
            
    elif choice == "c":
        every_year = copy.deepcopy(alpha_list)
        every_player = overall (every_year)
        all_players (every_player)
        print()
        
    elif choice != "q":
        # If the user enters any choice other than "a", "b", "c", or
        # "q", tell them that they enters invalid input and to
        # try again.  
        print("Illegal choice.  Try again. ")
        print()
    else:
        # If user enters "q", thank them for using
        # the program and close the file.  
        print("Thanks for playing! ")
        dataFile.close()


