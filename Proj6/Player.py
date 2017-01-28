#Player.py

class Player (object):
    def __init__ (self, first, last):
        '''the constructor for a player'''
        self.first = first
        self.last = last
        self.rating = 0
        self.info = []


    def update(self, team, year, comp, att, yards, tds, itcs):
        '''create a list of information for this player for this year and 
append it to the info field. Then call calcrating.'''
        player_year = [year, team, comp, att, yards, tds, itcs]
        self.info.append(player_year)
        calcrating()


    def calcrating(self):
        '''go through all sub-lists in info adding up totals for comps, 
attempts, etc. Then calculate the overall rating for this player. Store it
in the instance variable "rating" '''
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
                inter_rate = 2.375 - ((inter/att) * 25)
                rate = (comp_rate + yard_rate + td_rate + inter_rate) / 6 * 100

                self.rating = rate
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


    def returnName(self):
        '''return the name of the player first last'''
        return (self.first + " " + self.last)


    def returnReverseName(self):
        '''return the name of the player as last, first'''
        return (self.last + ", " + self.first)


    def __eq__ (self, other):
        '''determine if this person's name is the same as the other person's
name'''
        return self.first + self.last == other.first + other.last
                

    def __lt__(self,other):
        '''determine if this person's name is less than the other person's
name alphabetically'''
        return self.last + self.first < other.last + other.first
                

    def __gt__ (self, other):
        '''determine if this person's name is greater than the other person's
name alphabetically'''
        return self.last + self.first > other.last + other.first


    def __str__(self):
        '''return a string of the person's name and their rating in a nice
format'''
        print("%s %s %s" % (self.first, self.last, self.rating))


    def calc(self, sublist):
        '''calculate a passer rating for one sub-list year in  the info list'''
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
            year.insert(0, rate)


    def printInfo(self):
        '''print individual year information about his player including each 
year's passer rating. The list should be in year order. Use calc to assist.'''
        self.info.sort()
        for year in self.info:
            calc(year)
            print(year[1] "in" year[4] "-" year[0])
