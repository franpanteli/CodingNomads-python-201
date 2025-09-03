import csv
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11}

output_file = open("file_counts_2.0.csv","w")
row = []
for i in count:
    row.append(str(count[i]))
countwriter_two = csv.writer(output_file)
countwriter_two.writerow(["Header text"])
countwriter_two.writerow(row)
output_file.close()

"""
    -> compared to using a context manager
        -> there is no indentation needed in the code when using this approach
        -> this means it is harder to see the code which is writing the file compared to the code which is not
    -> what we have missing from the csv file
        -> a header
"""