"""What is a Python Generator Video Notes
    -> generator objects
    -> gen = [x for x in range(5)] <- list comprehension
    -> gen = (x for x in range(5)) <- generator (with parentheses, not braces)
    -> printing this returns a generator object, not the values of the elements in the (for example, list)
    -> the elements in the generator object are created as we iterate through them
    -> you can iterate through a generator object
        -> for num in gen:
            print(num)
            -> WE ARE CREATING AN ITERABLE, WHICH WE CAN ITERATE THROUGH
            -> EACH OF THE ELEMENTS ARE CALCULATED WHEN THIS IS DONE
            -> this saves storage
            -> the elements are not stored in a list, they are generated / calculated as we iterate through the elements in the object
        -> RANGE(5) IS A GENERATOR OBJECT
        -> print(range(5), type(range(5))
        -> GENERATORS, COMPARED TO LISTS, DON'T USE A LOT OF MEMORY AND COMPUATIONAL EFFORT
            -> they only uses memory when the code is run
            -> this can be useful for larger datasets
    -> we create generators in the same way as list comprehensions, just with curved brackets and not square ones (lists)
    -> they are objects of type generator, WE CAN ONLY SEE ELEMENTS IN THEM BY ITERATING THROUGH THEM WITH FOR LOOPS
    -> range() IS AN EXMAPLE OF THIS, IT ONLY WORKS LIKE A GENERATOR
"""