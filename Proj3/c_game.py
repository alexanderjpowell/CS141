dataFile = open("dictionary.txt", "r")

input_str = input("Enter a string of characters: ")
print(input_str)
length = len(input_str) - 1
for line_str in dataFile:
    line_strip = line_str.strip()
    line = line_strip.lower()
    count = 0
    countword = 0
    for char in input_str:
        var = 0
        for char1 in line:
            if char1 == char:
                var = 1
        count = count + var
    if count == length:
        countword += 1
        print(line)
if countword == 0:
    print("There are no words that match this criteria. ")
dataFile.close()
