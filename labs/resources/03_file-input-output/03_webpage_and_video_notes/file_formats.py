"""
    -> CSV stamds for comma separated values
    -> common file formats <- .csv, .xml, .json
        -> these are for data storage and exchange
        -> Python has modules to handle these
    -> this course includes csv now and json later
        -> .json is for data exchange over the internet
    -> summary
        -> open() with read mode, "r"
        -> then the .read() method to read the content of the file
        -> there are other file format types <- CSV, XML, JSON
"""

file_input = open("hello.txt", "r") #open the file in read mode
#r is the default

input_text = file_input.read() #use the read method to read the file contents
print(input_text) #this prints the file contents to the terminal
file_input.close()