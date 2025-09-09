# How can you call the function defined below using the given
# dictionary as its input.
# You shouldn't explicitly access the dict values, but use
# dictionary unpacking when passing the argument instead.

def congratulate(name, age):
    return f"Today {name} is {age} years old.\nHappy Birthday!"

user = {"name": "Adelheid", "age": 22}

print(congratulate(**user)) #this is dictionary unpacking, it uses a dictionary as an argument
    #for this to be the case, two stars are used when calling the function
    #two stars can be used or one, the output is the same
    #two stars is used for unpacking a dictionary and one is for unpacking an iterable list
