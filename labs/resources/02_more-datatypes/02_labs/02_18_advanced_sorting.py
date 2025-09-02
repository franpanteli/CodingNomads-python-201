# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

input_dict = {"item1": 5, "item2": 6, "item3": 1}

"""documentation
Key Functions¶
Both list.sort() and sorted() have a key parameter to specify a function (or other callable)
to be called on each list element prior to making comparisons.

For example, here’s a case-insensitive string comparison:

sorted("This is a test string from Andrew".split(), key=str.casefold)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
The value of the key parameter should be a function (or other callable) that takes a single
argument and returns a key to use for sorting purposes. This technique is fast because the key
function is called exactly once for each input record.

A common pattern is to sort complex objects using some of the object’s indices as keys. For example:

student_tuples = [
    ('john', 'A', 15), #student_tuples[2] is the age column
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    -> first the variable that stores the list of tuples
    -> then, the element in each of the tuples which we want it sorted by
    """

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
#we want to make the dictionary into a list of tuples, in this syntax:
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
#this way, it can be sorted

list_of_tuples = [(i,input_dict[i]) for i in input_dict]

# input_dict: {'item1': 5, 'item2': 6, 'item3': 1}
# list_of_tuples: [('item1', 5), ('item2', 6), ('item3', 1)]

result_list = sorted(list_of_tuples, key=lambda list_element: list_element[1])
    #this is a lambda function (later in the course)
print("input_dict =",input_dict)
print("result_list =",result_list)

    """lambda functions
        -> they are like list comprehensions, but for functions
    """