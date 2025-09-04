# Write the file counts to a `.csv` file.

#CONTENTS OF THE analyze.py file
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import csv

#open the file and read in the data
#store the data in the contents variable
filecounts_txt = open('filecounts.txt', 'r')
contents = filecounts_txt.read()
filecounts_txt.close()

#TO WRITE THE FILE COUNTS TO A .CSV FILE
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#open the csv file
filecounts_csv = open('filecounts.csv', 'w')
filecounts_csv.write(contents[1:len(contents)-1])
    #this is to write the contents of the txt file into the csv file
    #the indexing is to get rid of the { and }'s in the csv file
filecounts_csv.close() #close the csv file