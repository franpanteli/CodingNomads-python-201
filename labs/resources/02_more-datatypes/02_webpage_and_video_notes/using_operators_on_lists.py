a = [3, 0, 999, 42]
#don't work:
#print(a+2) #TypeError: can only concatenate list (not "int") to list
    #it can only add elements to the end of the list, not add 2 to every element

# print(a/2)TypeError: unsupported operand type(s) for /: 'list' and 'int'

# works:
print(a*2) #this gives two lots of the entire list, rather than multiplying each element by 2
    #we are operating on the entire list as one object
    #you would have to iterate through every element in the list and then divide it by 2
