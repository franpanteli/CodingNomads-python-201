"""Local scope
    -> global variables will exist locally, unless they are overwritten
    """

name = "Mycroft" #global variable

def print_name_box():
    print(name) #global variable accessed

    def smaller_box():
        # (Re)assigning a variable within a local scope
        # overwrites the same variable from an outer scope
        # You also can't use the global variable *before*
        # assigning it, if you assign it anywhere in that scope.

        # --TASK--: uncomment the print() function below
        #     and interpret the results when running the script

        print(name) #this returns an error, because the use of name below overwrites the global `name` variable
            #this one is then called before it is defined
        # UnboundLocalError: cannot access local variable 'name' where it is not associated with a value

        name = "Sherlock"

        def smallest_box():
            # Inner scopes always draw from the next outer layer.
            # After `name` got overwritten, the name that will
            # be printed is NOT the global-scope name anymore
            print(name)

        smallest_box()

    smaller_box()

print_name_box()

#there is a global and a local scope
#one variable can have different values, depending on the scope
#the next lesson is about the structure of a Python script
"""Summary
    -> there is a global and a local scope
    -> there can be nexted local scopes
    -> variables with global scopes have those values, unless they are overwritten on a local scope
    -> variables with local scopes take presidence over those with a global one
        -> they are more specific
"""
