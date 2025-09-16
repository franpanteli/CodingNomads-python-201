# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?
nums = range(1, 1000000)
# generator_expression = (i for i in nums if i % 1111==0) #from the previous question
generator_expression = (i for i in nums if i // 1111==0) #from the previous question

for i in generator_expression:
    print(i)

"""
    -> we get the numbers between 1 and 100000, divided by 1111, rounded down 
    -> these are all whole numbers 
    -> it is the same generator expression as in the previous question, except there is a floor division being used instead of a modulo
"""