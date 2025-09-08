def greet_many(greeting, *args):
    greetings = ""
    for name in args:
        sentence = f"{greeting}, {name}! How are you?"
        greetings += sentence + "\n"
        # print(type(args))
    return greetings

print(greet_many("hello", "Jay", "Fran")) #without printing the result of the function call, it is just returned
print(greet_many("hello", "Jay", "Neil"))

#THE TYPE OF ARGS IS A TUPLE, IT PUTS THE KEY WORD ARGUMENTS INTO THIS

"""-> you need to name the function something descriptive
        -> there is a specific format which you want the arguments to be in
            -> for example, you want the first argument to be a greeting and then for the rest of them to be the kwargs (keyword arguments)
            -> documentation is written for the function for this to be the case (this is next)
                -> docstring notation with functions
    -> summary
        -> *args <- used when defining a function with an arbitrary number of arguments
        -> **kwargs <- for key word arguments
            -> gathers all additional keyword arguments into a mapping
            -> this is also used to unpack collections and mappings when calling a function
            -> the arguments in kwargs are just stored in a tuple when the function is called
    """