"""Python Local Function Scope
    -> we wrote a greet() function and used docstrings
        -> these were three quotes which described arguments / the return of the function
        -> they could be accessed using the help() method when calling the function
    -> we also used type hints
        -> these return the data type of the argument which we want entered, or the data type which the function expects to return
    -> the greet function contains the greeting, name and sentence
        -> this lesson is about scope
        -> variables which are defined inside functions can only be accessed inside those functions
    -> Python local function scope
        -> you can call variables inside the function definition, but not outside of them
    """

def greet(greeting: str, name: str) -> str:
"""Generates a greeting"""
sentence = f"{greeting}, {name}! How are you?"
return sentence

print(name)
# OUTPUT: NameError: name 'name' is not defined

"""-> scopes
        -> when you use this method in VSCode, (three "'s), it asks you if you want to create a docstring
        -> you can't access those variables outside of the function
            -> you will get a name error if you try and print the values of the local variables globally
            -> this is to do with the scope of the variables
        -> to call the value of a variable defined in the function, it has to be returned
        -> next <- a walkthrough of scopes

    -> summary
        -> variables inside a function are local, to make them global the function has to return them 
    """
