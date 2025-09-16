# Create a Generator that loops over the given range and prints out only
# the items that are divisible by 1111.

nums = range(1, 1000000)

#done with a for loop
# for i in nums:
#     if i % 1111 == 0:
#         print(i)

#done with a list comprehension
list_comprehension = [i for i in nums if i % 1111==0]

#printed out result
# print(list_comprehension)

#converted list comprehension into generator expression
generator_expression = (i for i in nums if i % 1111==0)
# print(generator_expression)


