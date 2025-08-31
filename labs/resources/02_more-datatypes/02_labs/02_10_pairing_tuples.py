# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it
# with your mentor or chat about it on our forum.

    # This doesn't work, it's the code which the question came with
    # from resources import randlist
    # print(randlist)
    # We can define a list which does the same thing, using the random module

# Write your code below here

#to define randlist
import random
randlist = [random.randint(1, 100) for _ in range(9)]  # this is a list comprehension
    #it iterates through the numbers 1-10 and creates a list element between 1 and 100
    #this is a random list of numbers between 1-100, of length 10
print("The random list is: ", randlist)

##1 sorts the numbers
"""The difference between a method and a function
    -> a method is a function which applies to that one item
    -> a function has no dot
    -> .sort() <- method: this applies toone list and sets it equal to itself sorted
    -> sorted() <- function: this is when a list is a function of another list
    -> if you set a variable equal to randlist.sort(), it will return None, because you want a second list
        which is a function of the first (sorted()), not to apply a method to the origional list, which will
        change it
"""
print("The sorted list is: ", sorted(randlist))

#2 stores the numbers in tuples of two in a new list
sorted_list = sorted(randlist)
tuple_list = []
for index, value in enumerate(sorted_list):
    tuple_list.append((sorted_list[index], randlist[index]))
print(tuple_list)

#3 prints each tuple
print("These are the tuples in the list of tuples: ")
for i in tuple_list:
    print(i)

#4 If the list has an odd number of items, add the last item to a tuple together with the number `0`
if len(randlist) %2 != 0: #the length of random list is odd
    print("The last item of randlist together with 0 in a tuple: ",(0,randlist[-1]))
