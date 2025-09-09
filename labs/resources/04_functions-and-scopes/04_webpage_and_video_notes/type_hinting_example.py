"""-> this shows the type of data which the function expects as arguments, and to return
    -> you don't have to enter these datatypes, because the Python is dynamic and not static
        -> the code isn't told that the variable has to be a specific datatype 
    """

def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence
