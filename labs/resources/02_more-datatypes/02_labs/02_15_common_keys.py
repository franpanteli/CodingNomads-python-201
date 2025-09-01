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

#separate the dictionary one keys from values in separate lists
dict_1_keys = []
dict_1_values = []

for i in dict_1:
    dict_1_values.append(dict_1[i])
    dict_1_keys.append(i)

print("dict_1_keys: ", dict_1_keys)
print("dict_1_values: ", dict_1_values)

#do the same with the second dictionary
dict_2_keys = []
dict_2_values = []

for i in dict_2:
    dict_2_keys.append(i)
    dict_2_values.append(dict_2[i])

print("dict_2_keys: ", dict_2_keys)
print("dict_2_values: ", dict_2_values)











