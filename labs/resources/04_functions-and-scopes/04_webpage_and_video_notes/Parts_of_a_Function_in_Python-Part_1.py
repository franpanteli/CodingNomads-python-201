"""Parts of a function in Python
    -> the structure of a function definition
    -> parts of Python functions
        -> def
        -> function name
        -> parameters
        -> function body
        -> return statement
    -> def
        -> to define a new function
        -> def function_name():
    -> def function_name():
        -> function_name is a variable name
        -> this should be descriptive, and is used to call the function
    -> arguments
        -> these are also known as parameters
        -> these are optional, brackets (parentheses) are required
        -> ARGUMENTS ARE WHEN THE FUNCTION IS CALLED
        -> PARAMETERS ARE WHEN THE FUNCTION IS DEFINED
    """

def greet(greeting, name):  # PARAMETERS ARE ARGUMENTS IN THE DEFINITION OF THE FUNCTION
    pass

greet("Hello", "Martin")  # PARAMETERS ARE ARGUMENTS WHEN THE FUNCTION IS CALLED

#the order of positional arguments matters, or they will get passed to the wrong part of the function
    #the function can be called with keywords because of this:
greet(name="Martin", greeting="Hello")

"""-> Python can define keyword arguments with default values
    -> the keywords need to match the parameter name that the argument is referred to with in the functino body
    -> POSITIONAL ARGUMENTS ARE FUNCTION ARGUMENTS WHICH DON'T HAVE DEFAULT VALUES
    -> if a default value is used, then the variable name doesn't have to be called when the function is used
    """

# TO DEFINE A FUNCTION WITH DEFAULT VALUES
def greet(greeting="Hi", name="User"):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet())
print(greet(name="Fievel" greeting="Hello"))

# OUTPUT:
# Hi, User! How are you?
# Hello, Fievel! How are you?

#key word arguments have to be separated with a comma

"""-> you can pass different arguments to a function call
    -> they are assigned to different parameters (not arguments) in the function body
    -> def <- to define the function
    -> the function name
    -> PARAMETERS ARE VARIABLES IN THE DEFINITION OF THE FUNCTION
    -> positional and key word arguments
        -> one has a default and the other does not
    """