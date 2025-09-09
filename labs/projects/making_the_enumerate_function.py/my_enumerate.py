# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

"""
    -> this function should work in the same way as the Python enumerate function
    -> we want this as the output:

(0, 'Intro')
(1, 'Intermediate')
(2, 'Advanced')
(3, 'Professional')
"""

list = ['Intro', 'Intermediate', 'Advanced', 'Professional']

def my_enumerate(list):  # add your arguments
    #   add your code implementation
    #   pass
    index = 0
    for i in list:
        print((index,i))
        index += 1

my_enumerate(list)





