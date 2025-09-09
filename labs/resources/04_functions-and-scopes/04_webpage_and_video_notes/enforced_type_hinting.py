"""Enforced type hinting
    -> there are external packages, which make it possible to enforce static typing
    -> this forces the users to enter a specific datatype
    -> mypy is a package which has to be installed before it is used
    -> this forces the user to use a specific datatype for the argument of the function being defined

    -> for example, script_name.py
        -> the function would be defined in this .py file
        -> this returns an error message if the right datatype isn't used when the function is called
        -> it allows us to check that this is the case

    -> you can use type hints and mypy
        -> it tells you if there are some use cases which contradict the information encoded in the function's type hints

    -> you don't need to add type hints to the functions

    -> summary
        -> Python is a dynamically typed language
        -> this introduces potential errors
        -> type hints can be added to functions to document them better
        -> you can use external packages, e.g mypy, to enforce type hints and use Python more like a statically typed language
        -> you add the expected type of parameter after a colon
            -> you can also define the expected type of return value with an arrow, ->, at the end of the first line of the function definition

    -> the function is documented through a docstring as well as type hints
    -> scopes <- next
    """