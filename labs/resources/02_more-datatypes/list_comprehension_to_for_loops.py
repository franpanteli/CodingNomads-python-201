"""
List Comprehension Practice
    -> Search StackOverflow for code snippets that contain list comprehensions.
    -> Rewrite the list comprehensions as plain old for loops.
    -> Sets are next
    """

#EXAMPLE 1: From Stack Overflow
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python/231855#231855
mylist = [x*x for x in range(3)] #it creates a list, with square brackets
    #this is a list comprehension, because the for i in is backwards (it comes last)
    #the list contains x^2, from 1-3 (zero indexed)
for i in mylist:
    print(i)

#this is the same output as
output_list = [0,1,4]
for i in output_list:
    print("Mimicking Stack Overflow", i)

#EXAMPLE 2: Generated from ChatGPT
# Characters in a string
chars = [ch for ch in "Python"] #the entire thing is a list, because of the [] syntax
# → ['P', 'y', 't', 'h', 'o', 'n']

#this is the same output as
desired_output_string = "Python"
output_list_two = []
for i in desired_output_string:
    output_list_two.append(i)
print(output_list_two)

#this is two peices of code, which produce the same outcome
#normally, it's for i in, this is what we want, and then for i in

""" We can do this backwards:
desired_output_string = "Python"
output_list_two = []
for i in desired_output_string:
    output_list_two.append(i)
print(output_list_two)

we want ['P', 'y', 't', 'h', 'o', 'n']

desired_list = [ch for ch in "Python"]

You can also ask ChatGPT for more help with it
"""