# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

#we need to use for loops, to iterate over the two dictionaries
keys = []
values = []

for key in dict_1:
    if key in dict_2:
        keys.append(key)
        values.append(dict_1[key] + dict_2[key])
    if key not in dict_2:
        keys.append(key)
        values.append(dict_1[key])

for key in dict_2:
    if key not in dict_1:
        keys.append(key)
        values.append(dict_2[key])

result = dict(zip(keys, values)) #we zip the two lists and then make this into a dictionary
print("result =", result)


