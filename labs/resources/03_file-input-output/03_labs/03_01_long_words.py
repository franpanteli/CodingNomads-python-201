#TASK
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

#this txt file is in the same directory as the .py file
#we want to print those words to the console

#LOAD THE FILE AND STORE THE CONTENTS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#load the file
words_txt = open('words.txt', 'r') #we open the file and store it in a variable

#store the file contents in a variable
words = words_txt.read() #we store the contents in another variable

#RETURN THE WORDS WHOSE LENGTHS ARE > 20 CHARACTERS LONG
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

""" The split function 
    -> use split when it asks you to operate on individual words
    -> you can take an entire document and split it into different words
    -> this splits it into a list 
    -> you don't convert the contents into a list, you use the split function and then it does this 
    -> otherwise, I would have used a counter to iterate through the characters and separate them depending on 
        if the element being iterated through was a space
        -> I would have done this using the .isalpha() method
        
    list(words) <- this makes a list of characters 
    words.split() <- this makes a list of words, without whitespace
"""

list_of_words = words.split() #this is a list of words, excluding whitespace
#now we want to iterate through it, and print the ones whose length are > 20

for i in list_of_words:
    if len(i) > 20:
        print(i)

#this doesn't edit words.txt, because we are just printing out the words to the console whose lengths are >20
#and we close the file next, so it won't be compromised

    #CLOSE THE FILE
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
words_txt.close()