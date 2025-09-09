# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """
        What the function does:
            The function converts kilometers to miles.

        What arguments the function takes:
            The function takes a number of kilometers.

        What the function returns:
            The function returns kilometers in the function argument, converted to miles.
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__) #this returns the help() documentation for the function
    #this is the docstring which was written as part of this question
