# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

# desired output (cartesian product)
# [
#   ("neon orange", "S"),
#   ("neon orange", "M"),
#   ("neon orange", "L"),
#   ("spring green", "S"),
#   ("spring green", "M"),
#   ("spring green", "L")
# ]

#the same thing done with a for loop
# list = []
# for i in colors:
#     for j in sizes:
#         list.append((i,j))
# print(list)

#the same thing done with a list comprehension
    #to embed a for loop inside another loop, we use for i in list_name for j in other_list_name
output_list = [(i,j) for i in colors for j in sizes]
print(output_list)