# Use a lambda expression to sort a list of tuples based on
# the number value in the tuple. For example:
#
# unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
# sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

# syntax for sorted is different to map etc
print(sorted(unsorted_list, key=lambda x: x[1]))

"""
    -> print(list(filter(lambda x: x[0]=="M", names))) <- syntax from the previous exercise question 
    -> the key comes last, in this example it came first
    -> the list being filtered is the first argument in this case, and the second argument in the previous question 
        -> this was when the filter method was used 
        -> this can be used to filter for certain peices of information 
        -> this is different to sorting the list
            -> one takes the information and just takes certain peices, and another sorts all of the information there 
"""

#example from webpage
# ingredients = [("carrots", 2), ("potatoes", 4), ("peppers", 1)]
# print(sorted(ingredients, key=lambda x: x[1]))