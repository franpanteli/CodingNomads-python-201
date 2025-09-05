"""Functions
    -> open() <- this creates file objects
    -> concept
        -> composition <- breaking up the code
        -> DRY <- Don't Repeat Yourself
        -> procedural scripts <- from top to bottom
        -> a function is a script
        -> executing the instructions and giving you results
        -> avoiding repeating code
    -> to write functions
        def my_func(parameter): #to define the function
        pass # Replace with code that does something
        return  # Followed by a value that the function gives back
        -> return returns the function output
        -> parameter is the input of the function
        -> pass <- the function returns none if there is no output
    -> functions which have already been used in the course
        -> the maximum and minimum functions (example below)
"""

list = [1,2,3]
print(max(list))
print(min(list))

#functions which require parameters
for index, value in enumerate(list):
    print(index, value)
    #the enumerate function takes a list as an argument

#you can print out the value of a function to see if it returns a value, or None

"""
    -> functions are for breaking code into smaller sections
    -> generalising the instructions
        -> to reuse the code 
    -> the def keywords, then the function name / parameters / function body and return statement 
"""