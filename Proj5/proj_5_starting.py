# Project 5

import copy

def main():

    dataFile = open("passers_new.csv", "r")

    alpha_list = info(dataFile)

    rating_list = copy.deepcopy(alpha_list)
    best = passer_rating (rating_list)

    best_input = copy.deepcopy(alpha_list)
    tuple_func_input = passer_rating (best_input)
    output = player_dict_func (tuple_func_input)
    
    best_input2 = copy.deepcopy(alpha_list)
    tuple_func_input2 = passer_rating (best_input2)
    output2 = team_dict_func (tuple_func_input2)

    some_var_name = copy.deepcopy(alpha_list)
    something = overall (some_var_name)
    
    choice = ''
    while choice != "q":
        print("Menu Choices: ")
        print("a) Find a passer and print his career information and overall rating.")
        print("b) Find a team and print all the passers by year. ")
        print("c) Print a list of players and their ratings in alpha order. ")
        print("q) Quit ")
        print()

        choice = input("Enter choice: ")
        print(choice)
        print()
        choice = choice.lower()

        if choice == "a":
            first = input("Enter the player's first name: ")
            print(first)
            last = input("Enter the player's last name: ")
            print(last)
            print()
            name = first + " " + last
            if name in output:
                response = output[name]
                print(response)
            else:
                print("This person is not in the database. ")
                print()

        elif choice == "b":
            team_input = input("Enter the team's initials: ")
            print(team_input)
            print()
            team = team_input.upper()
            if team in output2:
                response2 = output2[team]
                print(response2)
            else:
                print("This team is not in the database. ")
                print()
                
        elif choice == "c":
            all_players = sorter (something)
            print()
            
        elif choice != "q":
            print("Illegal choice.  Try again. ")
            print()
            
        else:
            print("Thanks for playing! ")
            dataFile.close()


def info (players):
    '''Sorts the list of players in alphabetical order. '''
    players.seek(0)
    players.readline()
    all_players = []

    for line in players:
        words = line.split(",")
        all_players.append(words)
    all_players.sort()

    return all_players

def passer_rating (players):
    '''Calculate the passer rating for each player.  '''
    best_players = []

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

    best_players.sort(reverse = True)
    return best_players

    '''for player in best_players:
        name = str(player[0]) + ", " + str(player[1])
        print("%-27s %-5.2f" % (name, float(player[3])))
    print()'''


def player_dict_func (players):
    '''Create a dictionary entry for this player (if he
doesn't already exist) with his name as key and a list
including the tuple (tuple with year, team, and rating)
you created as value. If he already
exists in the dictionary, append this new tuple to the list
of tuples in the value portion of the dictionary. '''

    my_dict = {}
    for player in players:
        first = player[1]
        last = player[2]
        name = first + " " + last
        tuple_test = player[5], player[4], player[0]
        key = name
        value = tuple_test
        my_dict[key] = value

    return my_dict


def team_dict_func (players):
    '''Create a dictionary entry for this team if it
doesn't already exist. Create of tuple of year, name and
rating. The entry should have the team as the key and
a list including this tuple as the value. If the team
already exists, then append this new tuple to the list
in the value portion of the dictionary entry. '''

    my_dict = {}
    team_base = []
    for player in players:
        team = player[4]
        first = player[1]
        last = player[2]
        name = first + " " + last
        tuple_test = player[5], name, player[0]
        key = team
        value = tuple_test
        if key in my_dict.keys():
            my_dict[key].append(value)
        else:
            my_dict[key] = team_base
            my_dict[key].append(value)
            
    return my_dict

def overall (players):
    
    old_name = []
    overall = {}
    list_count = 0
    
    
    for player in players:
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

            overall[players_name] = rate
            
            old_name = player[0:2]
            old_info = player[5:]
            base_info = player[0:5]
            players_name = player[0] + " " + player[1]
        
        #for the first and only the first player entry set up old and base 
        #information without triggering a calculation of rating
        else:
            old_name = player[0:2]
            old_info = player[5:]
            base_info = player[0:5]
            list_count = 1
            players_name = player[0] + " " + player[1]

    return overall
    
def sorter (total_dict):

    my_list = []
    for key in total_dict.keys():
        name = key
        rate = total_dict[key]
        player_info = [name, rate]
        my_list.append(player_info)
    my_list.sort()

    for player in my_list:
        name = player[0]
        name_str = str(name)
        name_list = name_str.split(" ")
        player.extend(name_list)
        player.pop(0)
        last = player.pop(2)
        player.insert(0,last)
        first = player.pop(2)
        player.insert(1,first)
    my_list.append(player)
    my_list.sort()

    for player in my_list:
        print("%-15s, %-15s %30.2f" % (player[0], player[1], player[2]))
        # remake the list to have last,first just one entry (then print)




    
main()
