"""-> Python variable scope
        -> scope
            -> a name-binding (an association of a name to an entity)
            -> the region where the name-binding is valid
            -> it can be unbound
        -> variable scopes
            -> a box inside a box
            -> different scopes can be filled with different variables
            -> there is a global scope and a local scope
                -> to do with accessing the values of variables
            -> global scopes
                -> variables defined in the global scope are accessible in the local scope
                -> nested scopes
    """

name = "Mycroft" #this has a global scope and can be accessed anywhere in the script

def print_name_box(): #define a function
    print(name) #the global variable is accessible locally

    def smaller_box(): #define a nexted function
        print(name)

        def smallest_box():
            print(name)

        smallest_box()

    smaller_box()

print_name_box() #the global variable is accessible at every level
#UNLESS THEY ARE OVERWRITTEN
