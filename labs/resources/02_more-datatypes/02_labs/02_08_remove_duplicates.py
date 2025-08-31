# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
list_ = [1, 2, 3, 4, 3, 4, 5]
print("By converting to a different datatype: ", list(set(list_)))

# 2. Use a loop and a second list to solve it more manually
returned_list = []
for i in list_:
    if i not in returned_list:
        returned_list.append(i) #this adds i to returned_list
                                #you don't set returned_list equal to returned_list.append(i),
                                #because this method adds i

print("By using a loop: ", returned_list)

