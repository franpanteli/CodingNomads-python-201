"""
    -> tuples are immutable collections
    -> strings are immutable, you can't change them but you can make new ones
    -> they can be sliced using this [][]
        -> this is a method of extracting elements
        -> the end index is NOT INCLUDED
    """

tup = (1, 42, "hello!") #tuple
tup2 = tup[:2] #from the start to the second element
print(tup2)  #

#Adding tuples
tup = (1, 42)
tup2 = (123, 999)
tup3 = tup + tup2
print(tup3)  # OUTPUT: (1, 42, 123, 999)

"""
    -> this doesn't add the elements of the tuples together, it appends them
    -> now we will have a new tuple of length 4 -> it's a new datatype to get used to
    -> this is done because they are immutable (they cannot change), so when you add them you just create a longer tuple which is the two (or more) concatenated
    -> this is not the same as adding coordinates
    -> their values can be overwritten and they can be used to store different datatypes
    -> they can contain any datatype as an element
    -> unlike lists, the elements of tuples cannot change (they are immutable)
    -> tuple (), list []
"""