"""Python List, Set, & Dictionary Comprehensions Webpage Notes
    -> Python list, set and dictionary comprehensions
    -> they are a shortcut for `for` loop logic
    -> dictionary, list and set comprehension
"""

#Other comprehensions of x*2
listcomp = [x*2 for x in range(5)] #[0, 2, 4, 6, 8]

"""List comprehhension:
    -> this is the same as 
    empty_list = []
    for i in range(5):
        empty_list.append(2*i)
    -> a list of numbers from 0*2-5*2
"""

setcomp = {x*2 for x in range(5)}

"""Set comprehension:
    -> this is the same text as in the list comprehension 
    -> instead of using [], a set is used {}
    -> sets are immutable, so the shorthand for this couldn't use the .append method
    -> sets do not contain duplicate values
"""

dictcomp = {k: v*2 for (k, v) in {"a": 1, "b": 2}.items()}

"""Dictionary comprehension:
    -> the dictionary comprehension for x^2 is more complicated
    -> the keys and values 
    -> we have a dictionary, which contains the keys 
    -> the values are then some transformation of this 
    -> for keys, values in dictionary 1's items 
        -> key: 2*value 
        -> the form of the dictionary (with {} syntax) is key: 2*value 
        -> this is the syntax we want the dictionary (comprehension) in
        -> for the keys and values in this first dictionary 
    -> it's not that the values are some transformation of the keys, it's that the keys and values are a transformation of some other dictionary 
    -> we iterate through the items in another dictionary 
        -> and then the keys are 2* the values (in this example) 
"""

dict_1 = {"a": 1, "b": 2} #a dictionary is defined
dict_2 = {k: v*2 for (k, v) in dict_1.items()} #we are creating a new dictionary which applies a calculation to each of the elements in another dictionary
    #the values are the keys, just transformed

print(dict_2) # {"a": 2, "b": 4}

"""
    dictcomp = {k: v*2 for (k, v) in {"a": 1, "b": 2}.items()}
                                    [       x       ]
                                    -> x is a dictionary which we are iterating through 
                                    [            y           ]
                                    -> y is the items in this dictionary 
              [    z   ]
              -> the keys in the dictionary are the same as the keys in the basis dictionary 
              -> the values are the same as the other ones, but timsed by 2
                       [     a    ]
                       -> we are iterating through the keys and values in the other dictionary to get the values of this one

    Summary 
    -> next <- generator objects 
    -> there are different types of comprehensions  
        -> list, set and dictionary comprehensions
    -> you can use for loops for them as well 
    -> they are less readable, but more concise
"""