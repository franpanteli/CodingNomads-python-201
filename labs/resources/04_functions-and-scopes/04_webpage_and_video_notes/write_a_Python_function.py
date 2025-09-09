"""-> function building
        -> including calling the function
        -> he is writing .capitalize() in a function
        -> this is an in-built Python function
        -> def capitalize_words():
            pass
    """

def capitalize_words(test); #test is the argument, and all of the local variables inside it are parameters
    headline_list = [] # an empty list
    for words in text.split(): #convert the input string into a list of strings
        cap_word = word.capitalize() #this capitalises a single word
        headline_list.append(cap_word) #adds that single word to the initially empty list
    return " ".join(headline_list) #join the list of capitalised strings together in another string
        #return that