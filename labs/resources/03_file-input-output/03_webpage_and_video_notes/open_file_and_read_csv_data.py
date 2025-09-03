"""
    -> running the file twice outputs this in a csv format:

    8,2,2,11
    8,3,2,14

    -> this is based on the previous project, which counts the different number of file types on the desktop
    -> changing the contents of the desktop will change these numbers
    -> if new file types are added to the desktop, they won't be added to the csv file
    -> running the script each time adds a new line to the file, because it is in append mode
    -> you can use the previous project, which counts the number of different file types on the machine and have it write out the data to a csv file
        -> this can be done with a CSV, rather than a txt file
        -> this is done by changing the file type from .txt to .csv in the file
"""

# analyze.py
import csv #import the csv module

with open("filecounts.csv", "r") as csvfile: #use a context manager
    # -> this creates a new csv file, in read mode
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"]) #reads the elements of the dictionary
"""
    -> it is creating a dictionary from the output
    -> this reads the rows from a CSV file
    -> it normally uses the first row as the collumn name
    -> this time, we are assigning each row to the keys which we have provided
        -> we do this because we didn't add a header row to the CSV data
        -> the fieldnames are the keys for the dictionary that are made from each row of the data
"""
    counts = list(reader) #this is for printing the file output in the terminal
    #this is so that it outputs a list
print(counts) #print the file output in the terminal

""" Output:
[{'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}, {'Folder': '8', 'CSV': '2', 'MD': '2', 'PNG': '11'}]
    -> this is a list of dictionaries
    -> each of the elements can be accessed through a dictionary lookup
    -> next lesson
        -> including Path() objects from the pathlib module into the file I/O operations
    -> summary: open file and read CSV data
        -> a context manager can be used, with `with`
        -> this can be used to read data from files
        -> the `csv` module has the csv.DictReader() method
            -> this can be used to create data structures from the CSV data
"""