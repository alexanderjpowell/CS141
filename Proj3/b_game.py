dataFile = open("dictionary.txt", "r")

for line_str in dataFile:
        line_str = line_str.strip()
        line_str = line_str.lower()
        count_i = 0
        count_j = 0
        count_t = 0
        count_x = 0
        count = 0
        for char in line_str:
                if char == "i":
                        count_i += 1
                elif char == "j":
                        count_j += 1
                elif char == "t":
                        count_t += 1
                elif char == "x":
                        count_x += 1
        if count_i == 1 and count_j == 1 and count_t == 1 and count_x == 1:
                count += 1
                print(line_str)
if count == 0:
        print("no results")
        
dataFile.close()
