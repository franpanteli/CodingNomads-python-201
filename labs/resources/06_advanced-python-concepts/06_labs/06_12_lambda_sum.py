# Write a lambda expression that takes in three numbers
# and returns the sum of the numbers.

#with a regular function definition
# def sum_of_three(num_1, num_2, num_3):
#     return num_1 + num_2 + num_3

#writing the same function as a sum
                    # [arguments        ][operation           ]
sum_of_three = lambda num_1, num_2, num_3: num_1 + num_2 + num_3
print(sum_of_three(2, 4, 6))  # Output: 12

