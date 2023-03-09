#import os module
import os # allows for operating system / file handling functions

# import module for csv files
import csv
# import csv # functions to intraverse through csv files, go through rows as a series of lists

# general file path to our contacts.csv - 
#../Resources/contacts.csv

# instead, we use os.path.join to form a path to the csv file
csvFilePath = os.path.join("..", "..", "Resources", "contacts.csv")

# use the with open() functino to open the csvFilePath into an object
with open(csvFilePath) as csvFile:

#csv module .reader() function specifies the delimiter and object name for the reader in the open() function
        csvReader = csv.reader(csvFile, delimiter=",")

        # the csvReader has the info in the file, split into rows of lists
        #that correspond to each row of data in the file
        for row in csvReader:
                print(row)