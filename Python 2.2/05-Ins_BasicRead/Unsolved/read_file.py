# store the relative file path into a variable
filepath = "..\Resources\input.txt"

# use .open() function and pass in the file path, and "r" for readmode to read our file


with open(filepath, 'r') as textFile:

    # store all text into a variable named lines
        lines = textFile.read()

        print(lines)
