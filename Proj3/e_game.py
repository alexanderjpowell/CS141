# Palindrome - game E

dataFile = open("dictionary.txt", "r")
input_length_str = input("Enter length of the desired word: ")
input_length = int(input_length_str)
count = 0
for line in dataFile:
    line = line.strip()
    line = line.lower()
    length = len(line)
    if line == line[::-1] and input_length == length:
        count = count + 1
        print(line)
if count == 0:
    print("There are no words that fit this criteria. ")
dataFile.close()
