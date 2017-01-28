import random

# Code for game
countw = 0
countl = 0
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total1 = die1 + die2
if total1 == 7 or total1 == 11:
    game_status = "won"
elif total1 == 2 or total1 == 3 or total1 == 12:
    game_status = "lost"
else:
    game_status = "continue"
    first_roll = total1
while game_status == "continue":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total2 = die1 + die2    
    if total2 == first_roll:
        game_status = "won"
    elif total2 == 7:
        game_status = "lost"
    else:
        if game_status == "won":
            countw = countw + 1
        else:
            countl = countl + 1
        print(countw)
        print(countl)
# Final Code
count = 0
number_of_games_str = input("Please enter the number of games you would like to play.")
number_of_games = int(number_of_games_str)
for x in range(0,number_of_games):
    hey = countw
    if hey == 1:
        count = count + 1
# Experimental Probability
print("The chance of winning is", (((count)/number_of_games)*100), "percent.")
# Number of games played
print("The number of games played is: ",number_of_games)
# Number of games won
print("You won", count, "games.")
print(countw)
print(countl)