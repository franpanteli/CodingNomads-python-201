    """WEB PAGE NOTES - WHAT IS A PYTHON DICTIONARY
        -> the syntax for a Python dictionary is the same as an empty set ({})
        -> dict
            -> MAPPINGS (collections) of key-value pairs
            -> my_dict = {"greeting": "hello", "name": "martin"}
                -> it's like a lot of different variables and their values
                -> this is a brace {}, parentheses ()
                -> the syntax is key and value, and the value can be many different datatypes
                -> the keys have to be immutable datatypes, and unique (there can't be duplicates)
        -> dictionary lookups
            users = {"mary": 22, "caroline": 99, "harry": 24}
            print(users["mary"])
            -> to access the value(s) stored by the "mary" key
            -> it looks like accessing an element stored at that index of a list
        -> to change a dictionary value
            users = {'mary': 22, 'caroline': 99, 'harry': 24} #this is the dictionary
            users['harry'] = 20 #changing the value with the `harry` key
            print(users['harry']) #printing out the changed value
            # OUTPUT: 20
            -> dictionaries are mutable (their values can be changed)
            -> this can create aliasing errors
                -> this is when two variables are set equal to the same key
                -> change part of the dictionary by using one variable, and then accessing the dictionary through the other variable will lead to visible changes
                -> an alias is a name
            -> to create a new key in the dictionary, write Python to express the value of the elements at that key which doesn't exist are
                -> in doing this, the key-value pair will be created
                    users = {'mary': 22, 'caroline': 99, 'harry': 24} #defines dictionary

                    users['ludvik'] = 9 #sets the element with the key of 'ludvik' equal to the value of 9
                    print(users['ludvik']) #prints out the result and (below) the changed dictionary
                    # OUTPUT: 9
                    print(users)
                    # OUTPUT: {'mary': 22, 'caroline': 99, 'harry': 24, 'ludvik': 9}
    """

    """VIDEO NOTES - WHAT IS A PYTHON DICTIONARY
        -> {} <- these are curly braces
        -> they can be stored by variables
        -> dictionary_name["key"] <- this will retreive the data stored by this key
        -> they are mutable (changeable), values can be assigned to them
        -> this is not the same as an SQL database
        -> keys are immutable and values can be anything
            -> lists can't be used as dictionary keys
            -> the keys can't be changed
            -> lists are unhashable (not immutable datatypes)
            -> values can be lists (composite values)
            -> there can't be more than one value per key, but a value can be a list which contains multiple values
        -> iterating through dictionaries
            -> iterates through the value of the keys
            -> to extract values from this, it's for key, value in my_dictionary.items()
            -> for k in dictionary_name.keys() <- this extracts the value of the keys
        -> datatypes <- int, float, string, tuple, list, set, dict
        -> everything is an object
            -> you can make your own datatypes
    """

    """WEBPAGE NOTES - PYTHON: ITERATE DICTIONARY
        -> you can access only keys or values
        -> dictionaries are iterable mappings

        users = {'mary': 22, 'caroline': 99, 'harry': 20} #dictionary example

        for user, age in users.items(): #for the key and the value, print this
            print(user, age)

        -> dict.items() <- this gives a list of tuple object to iterate over
        -> this iterates over the keys and values of the dicitonary
        -> to iterate over only the dictionary keys or values
            -> .items()
            -> to only iterate through the dictionary keys
                -> if you use for i in on a dictionary, then this will return the value of the dictionary keys only (not the values stored by them)
                -> for k in users.keys() <- iterating through the dictionary keys
                    -> to get this, you can just iterate through the dictionary, this will only iterate through its keys, not values
                    -> they have key-value pairs
            -> to only iterate through the dictionary values
                -> this is done using the .values() method
                -> for v in dictionary_name.values()
    """