"""Python Lambda Functions Webpage Notes
    -> outline
        -> lambda functions and normal functions
        -> anonymous functions
        -> functional programming
        -> summary
    -> LAMBDA EXPRESSIONS ARE ALSO CALLED ANONYMOUS FUNCTIONS -> THEY DON'T HAVE A DEF ... WHEN YOU USE THEM (literally no name)
    -> you can define functions in one line
    -> lambdas and normal functions
        -> regular function
            -> how lambda expressions relate to normal functions
            def square_root(x):
                return x**2
        -> lambda expression
            squared = lambda x: x**2
        -> both of these functions take arguments
        -> lambda expressions are another way of writing functions
        -> if you want to give the functions names, use the def approach of doing this
    -> ANONYMOUS FUNCTIONS
        -> LAMBDA EXPRESSIONS ARE CALLED ANONYMOUS FUNCTIONS, BECAUSE THEY DON'T HAVE NAMES
        -> THEY AREN'T DEFINED WITH THE DEF KEYWORD, THIS IS WHEN FUNCTIONS HAVE NAMES
        -> lambdas are supposed to be one-off uses as imputs to other functions
        -> this can be done before using a sort, for example:

ingredients = [("carrots", 2), ("potatoes", 4), ("peppers", 1)] #list of tuples
sorted(ingredients, key=lambda x: x[1]) #TO USE THE SORT FUNCTION ON A LIST OF TUPLES, WITH THE SECOND ARGUMENT TO THIS AS A LAMBDA FUNCTION (HOW WE WANT THE LIST ELEMENTS SORTED)

        -> this function is applied to each tuple in the list (the iterable)
        -> the second argument to the sorted function is how we are organising the list elements
        -> output: [('peppers', 1), ('carrots', 2), ('potatoes', 4)]
    -> functional programming
        -> functional programming is different from object-oriented programming
        -> lambda expressions look different
            -> they are not object-oriented
        -> YOU DON'T HAVE TO USE LAMBDA EXPRESSIONS, THEY CAN JUST BE USED AS A REPLACEMENT TO DEFINING FUNCTIONS
            -> THEY DON'T HAVE A NAME, AND SO ARE CALLED ANONYMOUS FUNCTIONS
            -> THEY AREN'T DEFINED WITH A NAME
        -> METHODS USED WITH LAMBDA FUNCTIONS: filter(), map() and reduce()
            -> filterm, map, and reduce according to this funciton
            -> do this to the elements in this list, according to said function

        squares = list(map(lambda x: x**2, range(10)))
        print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

                -> we are converting the map into a list
                -> this is the first method used in the code above
                -> we then have a mapping from lambda is 1-10, squared
                -> defining anonymous functions concisely
                -> this has an iterable range
                -> YOU NEED TO CONVERT THE OUTPUT OF map() TO A LIST, BECAUSE THE OUTPUTS OF filter(), map() and reduce() ARE GENERATOR OBJECTS
                    -> this is just in Python3
            -> you can do the same thing more concisley with a list comprehension

            squares = [x**2 for x in range(10)] #this is a list comprehension with the same answer as the lambda expression
            print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

                -> lambda functions are anonyous, and one line
                -> lambda expressions evaluate to a value
        -> lambda expressions in different contexts
        -> LAMBDA FUNCTIONS ARE USEFUL WHEN PASSING ONE FUNCTION AS AN ARGUMENT TO ANOTHER
    -> summary
        -> lambda functions pass logic to another function as an argument
        -> THEY ARE ANONYMOUS FUNCTIONS (DEFINED WITHOUT NAMES WITH THE DEF KEYWORD)
        -> the receiving function can apply this logic to all elements as an iterable
        -> THEY ARE USED IN FUNCTIONAL PROGRAMMING, PYTHON IS OBJECT-ORIENTED
        -> you can define a function object or use a list comprehension instead
"""














