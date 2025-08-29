"""
        -> lists are a data type
        -> mutable sequences of information - you can change elements of lists, but not characters in strings or elements of tuples
        -> [] syntax
        -> you can convert from tuples to lists via list(tuple) - then the brackets change
            -> this is a type conversion
            -> they are normally homogenous - the elements are the same datatypes, but don't have to be
        -> tuples are better for combining different datatypes, because they are immutable
    """

bucket_list = ["Go to the Taj Mahal", "Go to other monuments"]
print("First element:", bucket_list[0])  #everything is zero-indexed, first element
print("Last element: ", bucket_list[-1])

"""
        -> you can slice lists using the same method as with strings, but strings are immutable
    """

bucket_list_six_elements = [
    "Skydive over the Swiss Alps",
    "Dive with great white sharks in South Africa",
    "Hike the Inca Trail to Machu Picchu",
    "Camp under the Northern Lights in Iceland",
    "Paraglide off a cliff in New Zealand",
    "Explore a remote jungle in the Amazon"
]

print("Second element: ", bucket_list_six_elements[1], "Fourth element: ", bucket_list_six_elements[2], "Sixth element: ", bucket_list_six_elements[4])

#Iterating with lists
for i in bucket_list_six_elements:
    print(i) #i is in the list, it's printing out the list elements
    #it is better if lists only contain one datatype
    #lists [], tuples ()
    #you can convert a list to a tuple by using the list() method

    """
        -> you can use the len method on it, because it is a collection
        -> the type is a list
        -> it can also be indexed
        -> list methods
            -> list_name.append() <- this method adds to the list
                -> this can't be done with a character or a tuple, because the contents are immutable
            -> list_name.pop() <- this method sets the list equal to itself, with the last element gone
            -> slicing <- from the start to the end list)name[:1]
                -> [from:end]
                -> this works with tuples and strings
        -> you can mutate a list
        -> tuples are immutable and use (), lists aren't immutable
            -> you can change the elements of a list
    """

a = [1,2,3]
b = [1,2,3]
a == b #True
a is b #False, they are different objects
#you can change elements of / in them, because they are lists
#you can't do this with tuples:
b[0] = 1 #tuples are immutabl, but you can access elements from them like this [][]
    #in x part of x element