import random
# Roll the die
def rolldice():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    return total

# Code for game
def game():
    countw = 0
    countl = 0
    val = rolldice()
    if val == 7 or val == 11:
        game_status = "won"
    elif val == 2 or val == 3 or val == 12:
        game_status = "lost"
    else:
        game_status = "continue"
        my_point = val
    while game_status == "continue":
        total = rolldice()
        if total == my_point:
            game_status = "won"
        elif total == 7:
            game_status = "lost"
    if game_status == "won":
        countw = countw + 1
    else:
        countl = countl + 1
    return countw

# Final Code
count = 0
number_of_games_str = input("Number of games: ")
number_of_games = int(number_of_games_str)
for x in range(0,number_of_games):
    hey = game()
    if hey == 1:
        count = count + 1
# Experimental Probability
print("The chance of winning is", (((count)/number_of_games)*100), "percent.")
# Number of games played
print("The number of games played is: ",number_of_games)
# Number of games won
print("You won", count, "games.")
