count = {'': 8, '.csv': 2, '.md': 2, '.png': 11}

# New code that writes to a file
file_out = open("filecounts.txt", "w") #use the open method to open a new txt file, in write mode
    #"w" has to be with ""'s
file_out.write(str(count)) #use the write method on that file
    #the argument of this is the text that we want to write to the file
    #the argument of this has to be a string

file_out.write("\n") #write a new line
file_out.write(str(count))

file_out.close()
    #close that file
    #the new file shows in the same folder the .py file is in
    #running the script again gets rid of its current content

# 'append' mode
#file_out = open("filecounts.txt", "a") #a is append, unlike write mode
#append to this file; add to the end of it
#you can take line 4 in this file and change "w" to "a"
#we keep the previous information after each run
#append mode is for adding new content without getting rid of the old
#considering that the data we are adding is a string, regular string methods can be used for this
#the next lesson is for persistent file data
