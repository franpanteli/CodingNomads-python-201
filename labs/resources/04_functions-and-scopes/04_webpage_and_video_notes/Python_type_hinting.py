"""Python type hinting
    -> docstrings (three "'s) are for when you define functions
        -> this allows the help() method to be used on them
        -> the docstring text will be returned when using this function on them
    -> in the IDE, you can collapse sections of the code
        -> Python is a dynamically typed language
            -> you don't need to define what datatype a variable is / what datatypes a function can take as an input
        -> dynamic typing is duck typing <- you don't have to tell it the variable type
            -> the variable type can change
        -> static typing <- the variable has a specific type when it's created
            -> this is used in other languages
            -> every varaible has a specific type when created
                -> the variable type can't be changed once it's been created
                -> avoiding accidental messups in the code
    -> the greet() function we defined could take any sort of input type
        -> a function in a statically-typed language would return errors if specific datatypes were entered
        -> statically typed languages care about the datatype
            -> when you create variables, you have to tell the code what variable type you are using
            -> so, when functions are used with arguments, certain error messages can be thrown
        -> Python is dynamically typed
            -> type hinting is about bringing in elements of statically typed languages
    -> tpye hinting
        -> to immprove documentation on which types should be used when calling a function
        -> Python is still dynamically typed
            -> this means they are just hints (they aren't enforced)
            -> you add the expected type of a parameter after the colon
    """

def greet(greeting, name):
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence