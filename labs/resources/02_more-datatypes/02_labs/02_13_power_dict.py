# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}
number_we_go_up_to = int(input("Please enter a number: "))

#Note: we add one because it is zero indexed
keys = [(i+1) for i in range(number_we_go_up_to)]
values = [((i+1)**2) for i in range(number_we_go_up_to)] #via list comprehension; first written in a list

n = dict(zip(keys,values))
print(n)