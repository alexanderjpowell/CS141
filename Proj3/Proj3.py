# Alexander Powell
# ajpowell@email.wm.edu
# (804) 564-6153
# Proj3.py

# This program is composed of a number of word games, which all read
# from a text file named dictionary.txt.  The first game finds words
# with only one vowel and exluding a specific letter.  The second game
# finds words containing the letters i, j, t, and x.  The third game
# finds words containing all but one letter of a givens string that
# the user inputs.  The fourth game finds words containing all the letters
# of another word with a maximum length, and the fifth game finds
# palindromes of a particular length.  The game ends when the user
# enters q, thus ending the program.  If the user enters anything other
# than an appropriate menu choice, an error message is displayed.  

# Ask user which game they would like to play
print("Choose which game you want to play")
print("a) Find words with only one vowel and excluding a specific letter.")
print("b) Find words with i, j, t, and x.")
print("c) Find words containing all but one letter of a given string.")
print("d) Find words containing all the letters of another word with a maximum length.")
print("e) Find palindromes of a particuar length.")
print("q) Quit")
print()

# Open the dictionary.txt file to read from and have the user choose a game
dataFile = open("dictionary.txt", "r")
select_game_str = input("Enter a choice: ")
print(select_game_str)
print()
select_game = select_game_str.lower()

if select_game == "a":
    ''' In Game A, the program finds words with only one vowel and exluding
    a specific letter.  Begin by asking the user the length of the word
    they want and what letter to exclude. '''
    word_length_str = input("Please enter the word length you are looking for: ")
    print(word_length_str)
    word_length = int(word_length_str)
    excludeletter = input("Letter to exclude: ")
    print(excludeletter)
    print()
    count = 0
    for line_str in dataFile:
        # Strip the carriage return and lowercase the characters in the words
        line_str = line_str.strip()
        line_str = line_str.lower()
        if len(line_str) == word_length:
        # Initialize the counts for all the vowels and the letter
        # to be excluded.  
                countA = 0
                countE = 0
                countI = 0
                countO = 0
                countU = 0
                countExclude = 0
                count = 0
                for char in line_str:
                # Use if/elif/else structure to count the vowels
                # and excluded letter.  
                        if char == "a":
                                countA += 1 
                        elif char == "e":
                                countE += 1
                        elif char == "i":
                                countI += 1
                        elif char == "o":
                                countO += 1
                        elif char == "u":
                                countU += 1
                        if char == excludeletter:
                                countExclude += 1
                countTotal = countA + countE + countI + countO + countU
                # Add the counts together and return the line in
                # the file that matches the conditions.  
                if countTotal == 1 and countExclude == 0:
                    count = count + 1
                    print(line_str)
    if count == 0:
        print("no results")
                    
elif select_game == "b":
    ''' In Game B, the program finds words that contain
    the letters i, j, t, and x. '''
    count = 0
    for line_str in dataFile:
        # Strip the carriage return and lowercase the characters in the words
        line_str = line_str.strip()
        line_str = line_str.lower()
        # Initialize the counts for relevant characters
        count_i = 0
        count_j = 0
        count_t = 0
        count_x = 0
        for char in line_str:
            # Use for-loop to count the number of i's, j's, t's and x's
                if char == "i":
                        count_i += 1
                elif char == "j":
                        count_j += 1
                elif char == "t":
                        count_t += 1
                elif char == "x":
                        count_x += 1
        # Use if statement to check if the word matched the conditions.  
        if count_i == 1 and count_j == 1 and count_t == 1 and count_x == 1:
            count += 1
            print(line_str)
    if count == 0:
        print("There are no words that fit this criteria. ")
        
elif select_game == "c":
    ''' Game C finds words containing all but one letter
    of a given string. '''
    input_str = input("Enter a string of characters: ")
    print(input_str)
    print()
    length = len(input_str) - 1
    count_word = 0
    for line_str in dataFile:
        line_strip = line_str.strip()
        line = line_strip.lower()
        count = 0
        for char in input_str:
            char2 = 0
            for char1 in line:
                if char1 == char:
                    char2 = 1
            count = count + char2
        if count == length:
            count_word += 1
            print(line)
    if count_word == 0:
        print("There are no words that fit this criteria. ")
        
elif select_game == "d":
    ''' In Game D, the program finds words containing all the letters of
    another word with a maximum length. '''
    # Ask the user to enter the word for the program to examine.  
    word = input("Enter word: ")
    print(word)
    print()
    # Ask the user to enter the maximum length of the desired returned words
    input_length_str = input("What is the maximum length of the word you want? ")
    print(input_length_str)
    print()
    input_length = int(input_length_str)
    # Sort rearrange the letters in the word to compare with the
    # words in dictionary.txt
    sorted_word = "".join(sorted(word))
    count = 0
    for line in dataFile:
        # Strip the carriage return and lowercase the characters in the words
        line = line.strip()
        line = line.lower()
        word_length = len(line)
        sorted_line = "".join(sorted(line))
        # Check conditions to determine if the words in the file match
        # the criteria of the game and print the results.  
        if sorted_word in sorted_line and input_length == word_length:
            count += 1
            print(line)
    if count == 0:
        print("There are no words that fit this criteria. ")
        
elif select_game == "e":
    ''' Game E finds palindromes of a particular length. '''
    input_length_str = input("Enter length of the desired word: ")
    print(input_length_str)
    print()
    input_length = int(input_length_str)
    count = 0
    for line in dataFile:
        # Strip the carriage return and lowercase the characters in the words
        line = line.strip()
        line = line.lower()
        length = len(line)
        # Check conditions to determine if the words in the file match
        # the criteria of the game and print the results.  
        if line == line[::-1] and input_length == length:
            count += 1
            print(line)
    if count == 0:
        print("There are no words that fit this criteria. ")

elif select_game == "q":
    # If the user enters q, thank them for playing the game.  
    print("Thanks for playing. ")
else:
    # If the users enters anyting besides an a, b, c, d, e, or q, return
    # an error message to let them know their entry is invalid.  
    print("Error: invalid entry.  Try again. ")

# Close the dictionary.txt file
dataFile.close()

