# Game C
dataFile = open("dictionary.txt", "r")
my_str = input("Enter a string: ")
sorted_str = "".join(sorted(my_str))
for line in dataFile:
    line = line.strip()
    line = line.lower()
    sorted_line = "".join(sorted(line))
    length = len(sorted_str)
    if sorted_str in sorted_line:
        print(line)
dataFile.close()
