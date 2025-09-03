"""
    -> reading files with Python
    -> you can read information from a file into the program in Python
    -> you open the file, then read data from the file, then close it
"""

#this creates a file in read mode:
file_in = open("filecounts.txt", "r") #to read the counts.txt file
#"w", write
#"a", append to the end of it
#"r", read

contents = file_in.read() #to save the contents of the file to a variab;e
# print(contents)
# print(type(contents)) #the type is a string

# {'': 8, '.csv': 2, '.md': 2, '.png': 11}
# {'': 8, '.csv': 2, '.md': 2, '.png': 11}
# print(contents)

#find indices we want to split at
# for index, value in enumerate(contents):
    # print(index, value)
    # if value == "}":
    #     print(index)

#split them to form a dictionary
empty_list = [0,1]
empty_list[0] = contents[0:40]
empty_list[1] = contents[41:81]

print("contents (string):",contents)
print("empty_list (list of dictionaries):",empty_list)

file_in.close() #then close the file
    #it is a file object

#you can edit open the file, read the strings, and then edit / operate on them

