#we can import from a module, or import an entire .py file - THE .py FILE IS THE MODULE WE ARE IMPORTING
    #using code inside code
# from ingredients.py import carrot #THIS RETURNS AN ERROR MESSAGE
# from ingredients import carrot #from the ingredients.py file, import the value of the `carrot` variable
import codingnomads.ingredients as i #THIS IS AN ALIAS IMPORT
    #alias meaning, another word for the same thing
    #this import preserves the namespace of the package
    #. corresponds to each new directory in this
print(i.carrot) #carrot is an attribute of ingredients.py
#ANOTHER WAY OF DOING THIS, WHICH DOESN'T INVOLVE IMPORTING THE ENTIRE .py FILE

# print(carrot) #this prints the value of the carrot variable, defined in the ingredients.py file
    #this works for the first version of the module import
#importing like this can be used to call the value of variables in other .py files
#ingredients.carrot returns an error message

"""Summary
    -> this works for .py files which share folders with each other 
    -> we are importing one .py file into each other 
        -> import name_of_py_file_without_the.py
        -> then the value of imported variables can be called 
    -> you can import everything, or just use from ... import 
    -> you can also use alias imports, which means import xyz as yx
    -> next <- importing our own modules (.py files) with relative paths 
        -> that aren't in the same folder that they are being called in 
"""

def make_soup(argument):
    print("The argument is", argument)

    # cooked potato
    # carrot

    """
        -> even if you only import the carrot variable, it will still print out cooked potato and carrot 
        -> the CLI prints cooked potato, but Python hasn't imported the potato variable 
        -> importing code from a module executes the whole script 
        -> this runs and can produce some unexpected output
        -> PYTHON RUNS THE ENTIRE SCRIPT WHEN A VARIABLE IS IMPORTED
    """