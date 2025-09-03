"""
    -> the files on a desktop - {'': 8, '.csv': 2, '.md': 2, '.png': 11}
    -> folders have no extension
    -> files are a type of persistent memory
    -> writing to and reading from files
    -> writing to a file
        -> create or open a file
        -> write the data to the file
        -> close the file
        -> you open it, operate on it, and then put it away (close it)
    """

#open the file and store this in a variable
    #this creates the output.txt file if it's not there
    #open the file in write mode
    #opening it in write mode deletes its content if this already exists
    #open this file in write mode
file_out = open("output.txt", "w")
    #open is a function

#this writes the file
    #perform a method on the file
file_out.write('This is what you are writing to the file')
    #write is a method

#close the file
    #you can't delete the file in some cases if you don't do this
    #you might only see the old file contents if you don't do it
file_out.close()

#you can write Python objects to files
#the data can be overwritten each time the script is ran and it might not be well formatted


