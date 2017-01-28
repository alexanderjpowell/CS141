# Alexander Powell
# (804) 564-6153
# ajpowell@email.wm.edu
#
# CS141
# Proj2.py
#
# This code simulates the game of craps as many times as the user desires
# and then outputs the results for the number of times the die were tossed, 
# the frequencies and probabilities for landing on each face of the die, the 
# number of games won out of the total number of games played, and the 
# experimental probability of winning a game of Craps.  

# Import necessary libraries
import random

# Initialize the number of times the computer wins the game, 
# how many times the dice were thrown, and how many times individual face 
# values were thrown all to zero.  
count = 0
count_roll = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
# Input random seed and number of games played from the user.  
seed_str = input("Please enter the random number seed: ")
print(seed_str)
seed = int(seed_str)
random.seed(seed)
number_of_games_str = input("Please enter the number of games to play: ")
print(number_of_games_str)
number_of_games = int(number_of_games_str)

for x in range(0,number_of_games):
    win_count = 0
    # Roll the dice for first round of the game.  
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total1 = die1 + die2
    count_roll = count_roll + 2
    # Count the number of times individual face values are thrown.  
    if die1 == 1:
        count1 += 1
    if die1 == 2:
        count2 += 1
    if die1 == 3:
        count3 += 1
    if die1 == 4:
        count4 += 1
    if die1 == 5:
        count5 += 1
    if die1 == 6:
        count6 += 1
        
    if die2 == 1:
        count1 += 1
    if die2 == 2:
        count2 += 1
    if die2 == 3:
        count3 += 1
    if die2 == 4:
        count4 += 1
    if die2 == 5:
        count5 += 1
    if die2 == 6:
        count6 += 1        

    roll = total1
    # Play the first round of the game.  If a 7,11,2,3, or 12 is not rolled, 
    # continue rolling the dice.  Use Booleans, True and False to denote 
    # whether the game was won or lost.  
    if roll == 7 or roll == 11:
        game = True
    elif roll == 2 or roll == 3 or roll == 12:
        game = False
    else:
        game = "continue"
        total2 = roll
    while game == "continue":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total3 = die1 + die2
        count_roll = count_roll + 2
        # Continue counting the number of times individual 
        # face values are thrown.  
        if die1 == 1:
            count1 += 1
        if die1 == 2:
            count2 += 1
        if die1 == 3:
            count3 += 1
        if die1 == 4:
            count4 += 1
        if die1 == 5:
            count5 += 1
        if die1 == 6:
            count6 += 1
                
        if die2 == 1:
            count1 += 1
        if die2 == 2:
            count2 += 1
        if die2 == 3:
            count3 += 1
        if die2 == 4:
            count4 += 1
        if die2 == 5:
            count5 += 1
        if die2 == 6:
            count6 += 1
        # Check conditions to see if the second roll matches the first 
        # or adds to 7.  
        if total3 == total2:
            game = True
        elif total3 == 7:
            game = False
    if game == True:
        win_count = win_count + 1
    if win_count == 1:
        count = count + 1
# Calculate Probabilities
probability_1 = (count1 / count_roll)
probability_2 = (count2 / count_roll)
probability_3 = (count3 / count_roll)
probability_4 = (count4 / count_roll)
probability_5 = (count5 / count_roll)
probability_6 = (count6 / count_roll)
# Output Statements: number of games played, number of tosses of 
# the dice, the frequencies and probabilities of landing on each of 
# the 6 face values, the number of games won, and the experimental 
# probability of winning at Craps.  
print()
print("We simulated", number_of_games, "games of Craps. ")
print()
print("In all, a die was tossed", count_roll, "times.")
print("The numbers:             1        2        3        4        5        6")
print("%-15s %8.0f %8.0f %8.0f %8.0f %8.0f %8.0f" % ("Their frequencies: ", 
                                                     count1, count2, count3, 
                                                     count4, count5, count6))
print("%-15s %-8.4f %-8.4f %-8.4f %-8.4f %-8.4f %-8.4f" % 
      ("Their probabilities: ", probability_1, probability_2, probability_3, 
       probability_4, probability_5, probability_6))
print("Of the", number_of_games, "simulated games, you won", count, "times.")
total_probability = count / number_of_games
print("%s %-.4f" % ("So the probability of winning at Craps is: ", 
                    total_probability))