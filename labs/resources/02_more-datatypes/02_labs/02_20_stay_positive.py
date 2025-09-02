# Use a list comprehension to create a list called `positive` from the list
# `numbers` that contains only the positive numbers from the provided list.

numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
positive = [] #[i for i in numbers if i > 0]

# for i in numbers:
#     if i > 0:
#         positive.append(i)

positive = [i for i in numbers if i>0] #the if statement goes at the end
#if statements go at the end of list comprehensions

print("Output: ", positive)



