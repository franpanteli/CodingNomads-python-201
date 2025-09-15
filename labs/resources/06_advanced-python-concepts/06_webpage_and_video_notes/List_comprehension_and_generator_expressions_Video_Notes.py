"""https://www.youtube.com/watch?v=ZoWgzG_r2qo
    List comprehension and generator expressions - Intermediate Python Programming p.4 Notes
    -> generators and memory
        -> they are generator expressions
        -> list comprehensions in generator expressions
        -> range
            for i in range(5) <- this is a generator
            -> it generates a string in the range of 0-5
            -> it doesn't save it into memory -> it just does it as we go along
        -> in Python2, range isn't a generator expression
        -> in Python3, we can get away with i = range(9999)
            -> this is a list and not a generator in Python2
        -> list comprehension is faster, but it uses the RAM to store the list
        -> generators are slower, because they are calculated as we go along
            -> but they use less memory, because they don't have to be stored
    -> to build generators
        -> list comprehensions
            -> xyz = [i for i in range (5)]
                -> this is the same as
                xyz = []
                for i in range(5):
                    xyz.append(i)
        -> generator expressions are the same, but they use brackets (parentheses)
        -> xyz = [i for i in range (5)] <- list
        -> xyz = (i for i in range (5)) <- generator
            -> this is not in the memory
            -> it is a generator object
            -> you can iterate through elements of the generator object to calculate / yield them
            -> it doesn't store the elements of the object when iterated through
                -> this saves memory
        -> lists can take storage
        -> generator objects are slower, because the elements in them are calculated as we go along
        -> he generates these objects and prints out the values by using a for loop
            -> they are fast to create, but take time when iterating through to print the values of
"""