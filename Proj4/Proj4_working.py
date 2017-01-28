#Proj4.py
#Code created by:Liam Canty, Lncanty@email.wm.edu, (757) 751-3151.

# class clarifications : can ignore the last, first. can use seek(0) to skip close and re open. List focus no dictionaries. Use functions. 

# The NFL is North America's professional men's football league.
# This program finds the best passers in NFL history, determined
# by a formula that computes the passer rating of all the players
# based on their statistics.  The program also outputs other
# statistics which include the player who passed for the most yards
# in a year, the player who passed for the most touchdowns in a year,
# the player who has the highest completions per attemped pass, and
# the player who got the most interceptions.  


import copy


# make a function that opens the doc, forms a list with data. calculates the rating puts it first in the list then appends the data to another list.

def sorter (meta):
    '''This function calculates the passer rating from a number of variables
and sorts the lists from best rating to worst, but only returns the top
50 players.  '''
    bestest= []
    for words in meta:
        att = int(words[7])
        complete = int(words[6])
        yards = float(words[11])
        touch = int(words[9])
        inter = int(words[12])
        c_rate = (((complete/att)*100) - 30) / 20
        y_rate = (yards - 3) / 4
        t_rate = (touch/att) * 20
        i_rate = 2.375 - ((inter/att) * 25)
        rate = (c_rate + y_rate + t_rate + i_rate) / 6 * 100
        words.insert(0,rate)
        del words[6:]
        bestest.append(words)
    bestest.sort(reverse = True)
    del bestest[49:]
    
    print("The top 50 passers based on their passer rating in individual years are: \n")
    print("%-9s %-10s %-5s %-21s %-5s" % ("Name", "","Year", "Rating", "Team"))
    for player in bestest:
        name = str(player[1]) + " " + str(player[2])
        
        print("%-20s %-5s %-20s %-15s" % (name, str(player[5]), str(player[0]), str(player[4])))

def info (master):
    '''The info function returns a list of lists for
every player in the csv file.  '''
    master.seek(0)
    master.readline()
    meta = []
    for line in master:
        words = line.split(',')
        meta.append(words)
    meta.sort()
                   
    return meta 

def average(players):
    '''If a player is listed in the csv file more than once the overall
function averages their passer rating and returns the top
20 players.  '''
    for player in players:
        
    
        

def yardage(players):
    '''The yardage function takes the list of all the players, pops
their passing yard values and inserts those values back into the beginnning
of each list.  It then sorts the lists in reverse order to find the
player with the maximum passing yards.  '''
    for player in players:
        sort_by = player.pop(8)
        player.insert(0,sort_by)
    players_test = copy.copy(players)
    sorted(player)
    a = sorted(players_test)
    players2 = a[::-1]
    bestest = players2[0]

    return bestest

def passtd (players):
    '''The passtd function takes the list of all the players, pops
their passing touchdown values and inserts those values back into the beginnning
of each list.  It then sorts the lists in reverse order to find the
player with the maximum passing touchdowns.  '''
    for player in players:
        sort_by = player.pop(9)
        player.insert(0,sort_by)
    players.sort(reverse=True)
        
    bestest = players[0]
        
    return bestest   

def comp_att (players):
    '''The comp_att function takes the list of all the players, pops
their completion and attemps values, divides them to find the ratio of
completions per attemp, and inserts that value back into the beginnning
of each list.  It then sorts the lists in reverse order to find the
player with the maximum completions per attempts.  '''
    for player in players:
        comp = int(player[6])
        att = int(player[7])
        sort_by = comp/att
        player.insert(0,sort_by)
    players.sort(reverse=True)
    
    bestest = players[0]
    
    return bestest

def lookup (first,last,lookup):
    master.seek(0)
    master.readline()
    meta = []
    for line in master:
        words = line.split(',')
        meta.append(words)
    meta.sort()
    for player in lookup:
        if first == meta[0] and last == meta[1]:
            return(first, last)
            

def main ():
    '''Executes the main program.  '''
    master = open("passers_copy.csv", "r")
    alpha_list = info (master)
    sort_list = copy.deepcopy(alpha_list)
    bestest = sorter(sort_list) 
    #print("%-20s %-5s %-8s %-5s" % ("Name", "Year", "Rating", "Team"))
    print(bestest)



    #overall_value = sorter(master)
    

    #overall = average(overall_value)
    #print(overall)
    yards_list = copy.copy(alpha_list)
    maxyards = yardage (yards_list)
    #print ("yards",maxyards)
    pass_list = copy.deepcopy(alpha_list)
    maxpasstd = passtd (pass_list)
    #print("td", maxpasstd)
    comp_list = copy.deepcopy(alpha_list)
    maxcomplete = comp_att (comp_list)
    #print ("c/a", maxcomplete)
    #print(alpha_list)
    
    '''choice = ''
    lookup_list = copy.deepcopy(alpha_list)
    while choice != 'n':
        choice = input("Are you interested in the overall rating of a player: ")
        print (choice)
        choice.lower()
        if choice == 'y':
            first = input("Enter the player's first name: ")
            print (first)
            last = input("Enter the player's last name: ")
            print (last)
            result = lookup (first,last,lookup_list)
            print(result)
        else:
            print("Invalid entry.  Try again. ")'''
    master.close()
main()
