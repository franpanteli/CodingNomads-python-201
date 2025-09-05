"""How to call a function in Python
    -> We have this function:

    def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

    -> executing the function
        -> this involves calling the function
"""

#defining the greet function
def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence #return the sentence output

#printing multiple different outputs from the function
    # print(greet("Hello", "World"))  # Hello, World! How are you?
    # print(greet("Howdy", "partner"))  # Howdy, partner! How are you?
    # print(greet("Zdravo", "prijatelj"))  # Zdravo, prijatelj! How are you?
    # print(greet("Hi", "Martin"))  # Hi, Martin! How are you?
#this takes two arguments
#it returns an error message if called without the arguments

# print(greet())
# TypeError: greet() missing 2 required positional arguments: 'greeting' and 'name'
#if calling the function without arguments, it returns error messages

# print(greet("hi")) TypeError: greet() missing 1 required positional argument: 'name'

# print(greet(4)) TypeError: greet() missing 1 required positional argument: 'name'

###THE ERROR MESSAGES THE FUNCTION COMES UP WITH
def greet(greeting, name): #defines the function
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

# Calling greet without passing any arguments
greet()

# results in an error - error when number is passed in
# TypeError: greet() missing 2 required positional - error with no arguments
# arguments: 'greeting' and 'name'

###SUMMARY
#you have to use the right arguments when calling a function, or it will return an error message
#the right amount of arguments are needed
#the function is called by its_name()