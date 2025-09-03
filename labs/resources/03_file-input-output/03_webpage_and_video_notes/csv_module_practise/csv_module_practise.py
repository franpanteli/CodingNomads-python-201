import csv
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)

#the output of this is
    #filecounts
    #then the contents of the dictionary
    #8,2,2,11

