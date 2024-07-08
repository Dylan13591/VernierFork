import sys

mergedFile = open("testFile.txt", "x")

for filename in sys.argv[1:]:   # For files in the sys.argv list, skip [0] as thats the python file            
    with open(filename, 'r') as file:   # Open file
        lineNumber  = 0
        if filename == 'vernier-output-0':
            for line in file:
                mergedFile.write(line)
                print(line)
        else:
            for line in file:               # Loop through each line of the file
                if lineNumber <= 5:
                    lineNumber += 1
                else:
                    mergedFile.write(line)
                    print(line)

mergedFile.close()