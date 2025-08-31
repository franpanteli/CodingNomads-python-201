# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
string = "codingnomads"
tuple = tuple(string)
print("Tuple: ", tuple)

# - Convert the tuple into a list.
list = list(tuple)
print("List: ", list)

# - Change the `c` character in your list into a `k`
for index, value in enumerate(list): #using enumerate removes the need for a
                                        #dummy boolean when iterating through lists
    if value == 'c':
        list[index] = 'k'

print("The list with c replaced as k is: ", list)
# - Convert the list back into a tuple.


