"""-> three ways to create tuples
        -> they are immutable and can be packed / unpacked
        -> tuples () vs arrays [] (one is coordinates)
        -> this creates the same tuple three times
    """
# Commas
tup1 = 1, 42, "hello!" #as a list in a variable name
print(tup1)  # (1, 42, "hello!")

# Parentheses
tup2 = (1, 42, "hello!") #as coordinates - this is the easiest method
print(tup2)  # (1, 42, "hello!")

# Tuple Function
tup3 = tuple([1, 42, "hello!"]) #to convert an array into a tuple, use the tuple() method
    #it's a constructor, not a method, because it does not use ., it actually builds things
print(tup3)  # (1, 42, "hello!")

#the length of a tuple is the number of elements it has, it's not the same as the length of one of those elements
#the tuple is the object storing those elements

for element in (1, 42, "hello!"):
    print(element) #you can iterate through tuples and print the value of the elements out (but you can't change them)
    #tuple unpacking, because they are immutable
    #they work with indexing and are zero indexed
    #they are ordered

    """
        -> this is a data structure
        -> they can contain strings and numbers (different data types)
        -> tuples don't actually need ()'s to be defined
        -> () these are parenthesis
        -> they are used for collections
            -> immutable collections
            -> usually heterogenious
            -> can be iterated through
    """

    #********************************
    """
        -> you can use [][] with tuples, to access the first element of the first elment, for example - [0][0]
        -> it's literally a coordinate system
    """
