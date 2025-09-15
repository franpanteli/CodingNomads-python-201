"""What is The Python Lambda Function Video Notes
    -> lambda expressions
    -> this is on Stack Overflow a lot
    -> lambda x: x+1 <- THIS IS A LAMBDA FUNCTION
    -> lam_sq = lambda x: x**2 <- you can assign them to variables
    -> THEY ARE ALSO KNOWN AS ANONYMOUS FUNCTION
    -> YOU AREN'T SUPPOSED TO SET THEM EQUAL TO VARIABLES, THEY ARE FUNCITONS
    -> def def_sq(x):
        return x**2
    -> print(lam_sq(3)) #9
    -> print(def_sq(3)) #9
    -> LAMDA FUNCTIONS DO THE SAME THING AS DEFINING A FUNCTION
    -> LIST COMPREHENSIONS ARE SHORTENED VERSIONS OF DEFINING LISTS WITH FOR LOOPS
    -> LAMBDA FUNCTIONS ARE SHORTER VERSIONS OF DEFINING FUNCTIONS
    -> LAMBDA FUNCTIONS ARE THE SHORTHAND FOR DEFINING YOUR OWN PYTHON FUNCTION
    -> THEY ARE FOR DOING FUNCTIONAL, AND NOT OBJECT ORIENTED PROGRAMMING
    -> locations = ["a", "b", "c"]
        -> wanting to sort the list by the last letter of locations alphabetically
        -> YOU CAN USE A LAMDA FUNCTION TO SORT LISTS
        -> print (sorted(locations, key = lambda x: x[-1]))
            -> the key is a lambda expression
            -> lambda expressions can be used in the key argument of the sorted method
            -> this is sorting the list from start until the penultimate method
    -> YOU CAN ACHIEVE THE SAME RESULT BY DEFINING YOUR OWN FUNCTION, OR BY USING A LAMBDA FUNCTION
        -> he does the same thing, but by defining his own function, instead of by using a lambda function
        -> this is
            def get_last_char(word):
                return word[-1]
        -> it is the last character in the sorted() function
    -> you can name the function something more descriptive if you use that method and not a lambda expression
        -> you can also annotate it with comments to get around this
        -> TO NAME A LAMBDA FUNCTION:
            key = lambda NAME_OF_FUNCTION: x[-1]
        -> you don't have to use lambda functions, you can write your own
"""