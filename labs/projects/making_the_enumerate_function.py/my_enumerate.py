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
# [(0, 'Intro'), (1, 'Intermediate'), (2, 'Advanced'), (3, 'Professional')]


"""What we want to define
    -> a function which returns a list of tuples
    -> the first element of the tuple contains the index
    -> the second element of the tuple contains the value of the list which we are iterating through
    -> the enumerate function does this:

0 Intro
1 Intermediate
2 Advanced
3 Professional

    -> we want the my_enumerate function to do the same
    -> we want to write a function called my_enumerate() function which takes this:

    list = ['Intro', 'Intermediate', 'Advanced', 'Professional']

    and converts it into this:

    [(0, 'Intro'), (1, 'Intermediate'), (2, 'Advanced'), (3, 'Professional')]
    """

# this is a function which takes a list and returns another list of this format:
    # [(0, 'Intro'), (1, 'Intermediate'), (2, 'Advanced'), (3, 'Professional')]
def my_enumerate(list):
    index_counter = 0
    return_list = []
    for i in list:
        return_list.append((index_counter, str(i)))
        index_counter += 1
    return return_list

# print(my_enumerate(list))
for index, value in my_enumerate(list):
    print("Index:",index)
    print("Value:",value)

#the my_enumerate function is about taking a list and converting it into a list of this format:
# ['Intro', 'Intermediate', 'Advanced', 'Professional']
# [(0, 'Intro'), (1, 'Intermediate'), (2, 'Advanced'), (3, 'Professional')]
#the my_enumerate() function can then be used in the same way as the enumerate() function
#this is an array of tuples





