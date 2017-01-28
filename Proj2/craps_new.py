# Alexander Powell
# Code to simulate multiple games of craps

import random

# Final Code
count = 0

count1_1 = 0
count2_1 = 0
count3_1 = 0
count4_1 = 0
count5_1 = 0
count6_1 = 0

number_of_games_str = input("Number of games: ")
print(number_of_games_str)
number_of_games = int(number_of_games_str)
for x in range(0,number_of_games):
    win_count = 0
    lose_count = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    if die1 == 1:
        count1_1 = count1_1 + 1
    if die1 == 2:
        count2_1 = count2_1 + 1
    if die1 == 3:
        count3_1 = count3_1 + 1
    if die1 == 4:
        count4_1 = count4_1 + 1
    if die1 == 5:
        count5_1 = count5_1 + 1
    if die1 == 6:
        count6_1 = count6_1 + 1

    val = total
    if val == 7 or val == 11:
        game_status = "won"
    elif val == 2 or val == 3 or val == 12:
        game_status = "lost"
    else:
        game_status = "continue"
        my_point = val
    while game_status == "continue":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total2 = die1 + die2        
        if total2 == my_point:
            game_status = "won"
        elif total2 == 7:
            game_status = "lost"
    if game_status == "won":
        win_count = win_count + 1
    else:
        lose_count = lose_count + 1
    if win_count == 1:
        count = count + 1
# Experimental Probability
print("The chance of winning is", (((count)/number_of_games) * 100), "percent.")
# Number of games played
print("The number of games played is: ",number_of_games)
# Number of games won
print("You won", count, "games.")
probability_1 = (count1_1 / number_of_games)
probability_2 = (count2_1 / number_of_games)
probability_3 = (count3_1 / number_of_games)
probability_4 = (count4_1 / number_of_games)
probability_5 = (count5_1 / number_of_games)
probability_6 = (count6_1 / number_of_games)
print(probability_1)
print(probability_2)
print(probability_3)
print(probability_4)
print(probability_5)
print(probability_6)