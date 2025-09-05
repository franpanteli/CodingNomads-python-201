#Now we have a Python function:
def capitalize_words(test): #test is the argument, and all of the local variables inside it are parameters
    headline_list = [] # an empty list
    for words in text.split(): #convert the input string into a list of strings
        cap_word = words.capitalize() #this capitalises a single word
        headline_list.append(cap_word) #adds that single word to the initially empty list
    return " ".join(headline_list) #join the list of capitalised strings together in another string
        #return that

#calling the function
text = "gator atttacks puzzle experts"
print(capitalize_words(text))
#this capitalises the first letter of each word in the input string
#different input still has the same functionality

#another way of doing this
    #Python has a string method which does this
text.capitalize() #capitalise the text
text.title() #this changes the string again, so that its first letter is capitalised (not the entire thing)

