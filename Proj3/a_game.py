dataFile = open("dictionary.txt", "r")

word_length = int(input("Please enter the word length you are looking for: "))
excludeletter = input("Letter to exclude: ")

for line_str in dataFile:
        line_str = line_str.strip()
        line_str = line_str.lower()
        if len(line_str) == word_length:
                countA = 0
                countE = 0
                countI = 0
                countO = 0
                countU = 0
                countExclude = 0
                for char in line_str:
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

                if countTotal == 1 and countExclude == 0:
                        print(line_str)
                                
        
dataFile.close()
