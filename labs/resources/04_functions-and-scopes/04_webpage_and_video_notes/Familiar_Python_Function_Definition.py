"""-> functions used before
            -> print()
            -> type()
            -> str(), int(), float(), list()
            -> input() <- this takes input from the user
            -> open() <- this opens a file
            -> you can write these functions
                -> they are automatically installed in Python
        -> functions have return values
            nstr = "42"
            n = int(nstr)
        -> you store the output of the function in a variable
        -> fruitful functions have outputs
            -> they return things which can be stored as varaibles
        -> void functions only have an output of None
            -> print()
            -> this displays an output to the console
            -> the output is a side effect
            -> you wouldn't print something and then store the print in a variable, because that's a void function
        -> if you return `print`, you get None
        -> functional programming is programming with functions that have returns
        -> FRUITFUL FUNCTIONS RETURN VALUES, VOID FUNCTIONS RETURN NONE
    """

# return print("Hi") #void function, None
# return type() #'return' outside function
# return str()
# return int()
# return float()
return list("hello")
# return input()
# return open()
    #the functions need arguments, you can't just try and return them