"""
        -> other dictionary methods
            -> dictionary_name.clear() <- to empty the dictionary
            -> other methods
                -> dictionary_name.get() <- returns the value stored at the argument key
                -> dictionary_name.pop() <- this removes a value from the dictionary whose key is the argument
                -> dictionary_name.update()
    """

example_dictionary = {'mary': 22, 'caroline': 99, 'harry': 20}

#the .get() method
    #get returns the value for the key if the key is in the dictionary
    #for example, let's tacke the 'mary' key - it should return 22

print(example_dictionary.get('mary'))

#the .pop() method
    #this removes the item if it is in the dictionary and returns its value
    #this is used to pop (remove) an element from the dictionary

#example
    #if we want to use this to remove caroline from the dictionary

print(example_dictionary.pop('caroline')) #this returns the value of the key
print(example_dictionary) #this returns the dictionary without its element

#the .update() method
    #this updates the dictionary with the key/value pairs from mapping / iterable kwargs
    #using this to change the age of Mary to 25

example_dictionary.update({'mary': 25}) #it makes no sense to print this (it's a method)
print(example_dictionary)

#using the documentation for this

    """summary of dicitonary methods
        -> dict.keys() <- iterates over the dictionary keys
        -> dict.values() <- iterates through the dictionary values
        -> dict.items() <- iterates over the dictionary keys and values
    """
