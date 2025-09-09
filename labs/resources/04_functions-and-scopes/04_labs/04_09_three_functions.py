# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def uppercase(input_string):
    return input_string.upper()

def lowercase(input_string):
    value = uppercase(input_string) #use the uppercase function in the lowercase function
    return value.lower()

def add_dot(input_string):
    value = lowercase(input_string)
    return value + '.'

print(add_dot("HELLO")) #the output is lowercase, no matter what the input is
    #a dot is added to the end of the input function


