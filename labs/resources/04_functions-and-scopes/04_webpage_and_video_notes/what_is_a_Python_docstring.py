"""Python docstrings
    -> to document what the functions do
        -> how to use and write them
    -> docstrings are to do with documentation
    -> working with functions
        -> they should describe three aspects of the function
            -> what they do
            -> what arguments they take
            -> what they return
    -> how to write good docstrings
        -> use three "'s
        -> this is done at the beginning of the function definition
    """

def greet(greeting, name):
    """Generates a greeting.

    Args:
        greeting (str): The greeting to use, e.g., "Hello"
        name (str): The name of the person you want to greet

    Returns:
        str: A personalized greeting message
    """
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

"""-> about docstrings
        -> the docstring includes information about how to use the function
        -> THE help() METHOD CAN BE USED TO ACCESS THE DOCSTRING
        -> doctrings are not just for multiple-line comments, THEY ARE FOR help(function_name)
        ->  this can also be accessed by using the .__doc__ attribute
        -> help(greet) is used in the terminal
        -> this is exited by using the q character
        -> this also works for standard functions, as long as they have docstrings
        -> DOCSTRINGS ARE ACCESSED VIA THE help() FUNCTION
        -> you can use the help() method on standard Python functions
        -> VSCode has an auto docstring plugin
        -> Tab can be used to write docstrings in a more automatic way

    -> summary
        -> they are comments after the function definition
        -> doubble or tripple quotes
        -> the style of them depends on the organisation you might be working for
        -> DOCSTRINGS ARE FOR help() DOCUMENTTATION WHEN DEFINING A FUNCTION
        -> they (aren't) just for function definitions
        -> they contain
            -> what the function does
            -> the arguments of the function
            -> what the function returns
        -> there are guidelines on how to write these
            -> this creates documentation for the code
            -> the documentation can be accessed by using the help() method on the function
        -> adding type hints to function definitions <- next
    """


