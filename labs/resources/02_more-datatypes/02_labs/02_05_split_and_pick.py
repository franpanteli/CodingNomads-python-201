# 1. Write a script that takes in a string from the user.
from collections import Counter #from the Python documentation
string = input("Enter a string: ") #takes user input
# string = "Hello world hello world world" #test

# 2. Using the `split()` method, create a list of all the words in the string
list_of_strings = string.split() #hello world goes to ['hello', 'world']

# 3. and print back the most common word in the text.
counter = Counter(list_of_strings) #this is adictionary with the word frequency
    #we want the key with the maximum value

print("The most common word is", counter.most_common(1)[0])

""" Dissecting counter.most_common(1)[0]
    counter <- this is a dictionary which contains the frequency that each word appears in `string`
            -> it is case sensitive
    counter.most_common(1) <- this is a tuple with the most common word and its frequency
"""

