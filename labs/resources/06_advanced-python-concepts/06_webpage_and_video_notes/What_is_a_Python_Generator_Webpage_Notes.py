"""What is a Python Generator Webpage Notes
    -> generator objects are similar to list comprehensions
"""

generator = (x*2 for x in range(5))

#this is the same as this:

"""
    list = []
    for i in range(5):
        list.append(2*i)
    
    -> but the output is not a list, it's a generator object
    -> the values are stored in the generator object
    -> it's not like something whose value you can print out, the numbers (in this case) which it stores, can't be printed
        -> this makes them more memory efficient 
        -> you can use list, set and dictionary comprehensions, but you can also define a generator object
    -> they use round brackets (parentheses) 
    -> you can't print out its values using the print method 
        -> classes and objects are later in the course
    -> you can work with iterables in a more memory-effective way
    -> this can be more efficient for larger datasets
"""

print(generator) #<generator object <genexpr> at 0x1106845f0>
print(type(generator)) #<class 'generator'>

#you can convert the generator object into a list, by changing the brackets in the generator definition
#this will let you see what values are stored by the generator object

"""
    -> memory 
        -> we need it to store the generator objects
        -> with larger lists, this is an issue 
        -> large datasets can use up all of the storage on your machine 
        -> a generator is a single generator object 
        -> THE GENERATOR ONLY YIELDS EACH ITEM OF THE ITERABLE ONCE
        -> IT IS DELETED ONCE IT ISN'T USED 
        -> this means they are SLOWER IN EXECUTION 
        -> they are faster to create
        -> THE GENERATOR ISN'T LIKE A LIST, WHERE THE ELEMENTS ALL EXIST AT ONCE -> THEY ARE CALCULATED 
        -> TO PRINT OUT THE ELEMENTS IN A GENERATOR OBJECT, YOU HAVE TO ITERATE OVER THE ENTIRE THING TO CALCULATE IT 
        -> IT'S NOT THAT ALL ELEMENTS EXIST AT ONCE, LIKE IN A LIST, THE ELEMENTS ARE CALCULATED AS THE OBJECT IS CALLED INTO EXISTANCE
        -> this can improve memory usage and therefore performance of the program at larger scales
    -> iterables 
        -> they are called iterables for this reason -> their elements can only be accessed by calculating them in a for loop
        -> their elements aren't all stored at once, for example as with a list
        -> THEY ARE CALLED GENERATOR OBJECTS, BECAUSE THEIR ELEMENTS ARE LITERALLY CALCULATED AS YOU GO ALONG 
            -> YOU CAN'T JUST ACCESS THE VALUE OF THESE ELEMENTS, THEY HAVE TO BE CALCULATED 
        -> this means they are memory-efficient 
        -> ITEMS IN GENERATORS ARE YIELDED, THIS MEANS THAT THEY ARE CALCULATED AS THE CODE IS RUN 
"""

gen = (x*2 for x in range(5)) #the generator contains the elements from (1-5)*2

for i in gen:
    print(i)

# OUTPUT:
# 0
# 2
# 4
# 6
# 8

"""Summary 
    -> the syntax for creating generator objects is similar to the syntax for list comprehensions 
    -> you aren't calculating all of the elements at once, this is only done when the code is ran 
        -> you are only creating one object
    -> this is useful for saving memory with large amounts of data
"""