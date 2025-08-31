# Convert a string to a tuple and print out the result.
string = "codingnomads"
print(tuple(string))

# What do you see?
    #('c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's')

# What happens if you try to iterate over your tuple of characters?
    #this creates a tuple, whose elements are all individual strings
tuple_of_characters = tuple(string)
print("Iterating through the tuple:")
for i in tuple_of_characters:
    print(i)

    #RESULT:
    # c
    # o
    # d
    # i
    # n
    # g
    # n
    # o
    # m
    # a
    # d
    # s

# Do you notice any difference to iterating over the string?
print("Iterating through the string:")
for i in string:
    print(i)
    #the result is the same when iterating through a tuple and string of the same word