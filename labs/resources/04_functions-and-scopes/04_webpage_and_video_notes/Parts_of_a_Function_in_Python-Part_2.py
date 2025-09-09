"""-> def function_name():
        indended code inside this block
        -> this is called the function body
        -> return
            -> this is what the function returns
            -> return ...
            -> this makes the function FRUITFUL
            -> OTHERWISE, NONE TYPE IS RETURNED
                -> THIS IS A VOID FUNCTION
            -> None will be returned if the function does not have a return statement and is not called
            -> printing inside the definition of the function is not the same as using a return statement
            -> you would have to print the return value
    """

def greet(greeting, name):
sentence = f"{greeting}, {name}! How are you?"
return sentence

print(greet("Hello", "World"))

"""-> this returns a value which we can work with
    -> the return value defines what we have access to
    -> everything inside the function is local, not global, and can't be accessed outside of the function call
    -> this is to do with scopes
    -> the data has to be wrapped in a tuple, for example, with the value and the index, if we want to make this easier
    -> VOID FUNCTIONS DON'T RETURN A VALUE
    -> FRUITFUL FUNCTIONS RETURN VALUES
    """
