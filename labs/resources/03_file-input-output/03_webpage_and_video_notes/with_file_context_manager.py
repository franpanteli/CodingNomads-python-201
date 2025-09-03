"""
    -> using CSV files with Python
    -> converting dictionary data to CSV files
    -> CSV is a Python module
    -> with is a shortcut to open and read files with Python
    -> sometimes, the file might not exist or its contents might not be as expected
"""
with open("filecounts.txt", "r") as file_in: #this is a context manager
                                        #the file is automatically closed at the end of the code block
    print(file_in.read())

"""
    -> CSV file creation
    -> CSV is Comma Separated Values, which is the same as a Python dicitonary
    -> Python dictionaries can be exported as CSV files
"""

import csv #import the CSV module from the Python standard library
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11} #a Python dictionary stored in the count vairable

with open("filecounts.csv", "a") as csvfile: #use a context manager to open a new file
        #this is a context manager, it opens the csv file and shuts it when done
        #this is a csv writer object
    #open a new csv file called filecounts and append information to it as a csvfile
    countwriter = csv.writer(csvfile) #use the writer method to write csv file
    data = [count[""], count[".csv"], count[".md"], count[".png"]] #list conmprehension to count the data in the csv file
        #accessing each peice of information in the dictionary using a lookup
    countwriter.writerow(data) #write the row information in the csv file


