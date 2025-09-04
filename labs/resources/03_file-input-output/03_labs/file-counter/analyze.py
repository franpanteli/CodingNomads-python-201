# Use the `csv` module to read in and count the different file types.
import csv

#open the file and read in the data
#store the data in the contents variable
filecounts_txt = open('filecounts.txt', 'r')
contents = filecounts_txt.read()
filecounts_txt.close()
