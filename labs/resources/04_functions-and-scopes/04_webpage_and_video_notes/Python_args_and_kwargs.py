"""Python args and kwargs
    -> introduction
        -> * <- args, arguments
        -> ** <- kwargs, key word arguments
        -> both are replaceable variable names
        -> * is a prefix
        -> this allows the function to take arbitraty numbers of arguments
    -> * <- args
        -> this is in the definition of a function
        -> all the passed in arguments are moved into a collection
            -> for example, a list which can be iterated through
            -> there can be any number of these (which will not crash the computer)
        -> example:

def print_args(*args):
    for a in args:
        print(a)

print_args("barcelona", "tahoe", "ubud", "koh tao")

# OUTPUT:
# barcelona
# tahoe
# ubud
# koh tao

        -> this is for multiple arguments
        -> * <- have any number of them (arguments)
        -> IT IS IN THE FUNCTION DEFINITION
    """

def print_args(*args):
    for a in args:
        print(a)

print_args("barcelona", "tahoe", "ubud", "koh tao")

# OUTPUT:
# barcelona
# tahoe
# ubud
# koh tao
def print_args(*args):
    for a in args:
        print(a)

print_args("barcelona", "tahoe", "ubud", "koh tao")

# OUTPUT:
# barcelona
# tahoe
# ubud
# koh tao

print_args("a", "b", "c")
#*ARGS IS ONLY USED IN THE FUNCTION DEFINITION

"""
    ->**kwargs
        -> PYTHON PACKAGES THE ARGUMENTS INTO A DICTIONARY
        -> this is in a mapping
        -> example

def print_kwargs(**kwargs):
    for k, v in kwargs.items(): #THE .item() METHOD IS USED FOR THIS
        print(k, v)

print_kwargs(country='ukraine', city='odessa')

# OUTPUT:
# country ukraine
# city odessa

            -> IT IS IN THE ARGUMENTS OF THE FUNCTION DEFINITION
            -> IT PUTS THEM INTO A DICTIONARY
            -> ** <- as many arguments as you want (within reason)
"""

def greet_many(greeting, *args): #the greet many function
    greetings = "" #what is returned

    #building out what is returned
    for name in args: #iterating through the arguments
        #we are iterating through the different names in args
        sentence = f"{greeting}, {name}! How are you?"
        greetings += sentence + "\n"
    return greetings

#for a web application

""" -> this takes a POSITIONAL ARGUMENT (WITHOUT *)
    -> * NEEDS TO COME LAST IN THE LIST OF ARGUMENTS IN THE FUNCTION DEFINITION
    -> *args arguments get put into a collection
    -> YOU CAN USE A LIST OR A TUPLE IN THE ARGUMENTS WHEN THE FUNCTION IS CALLED
    -> decorators are later
    """

