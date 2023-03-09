#import os module
import os # allows for operating system / file handling functions

# import module for csv files
import csv

# general file path to our contacts.csv - 
# ../Resources/contacts.csv

# instead, we can use os.path.join to form a path to the csv file
csvFilePath = os.path.join("..", "Resources", "contacts.csv")

# use the with open() functino to open the csvFilePath into an object
with open(csvFilePath) as csvFile:

    # csv module .reader() funtion specifies the delimiter and object name for the reader in the open()
    # reader in the open() funtion
    csvReader = csv.reader(csvFile, delimiter=",")

    # the csvReader has the info in the file, split into rows of lists
    # that correspond to each row of data in the file
    
    #if the first row has header data, use next() to pass over the row
    header = next(csvReader) # skips the first row and stores into a variable
    print(header) 
    print("--------")

    # read each row of data and display each row of data
    #for row in csvReader:
        #print(row)

print("----------------")
# print out first names (index 0) of each row
for row in csvReader:
        print(row[0])
        #for item in range(len(row))
        #   print(row[item])

# in order to write to a file, use with open(filepath, "w")

#outputFilepath = "../Resources/output.csv"

outputFilePath = os.path.join("..", "Resources", "output.csv")

with open(outputFilePath, "w") as csvOutput: