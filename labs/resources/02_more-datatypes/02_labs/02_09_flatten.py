# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = []
for i in starter_list:
    for j in i:
        flattened_list.append(j)
print(flattened_list)

# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

def flatten(nested_list): #this defines it as a function
    flat_list = [] #initialise flattened list
    for item in nested_list: #iterating through the argument list
        if isinstance(item, list): #if the item we are iterating through is a list
            flat_list.extend(flatten(item)) #flatten the item, and carry on flattening the item
        else:
            flat_list.append(item)  # otherwise, add that element to the returned list
    return flat_list
