# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(type_of_bread = "brown", *args):
    print(f"{type_of_bread} bread")
    for topping in args:
        print(f"A few of these: {topping}")
    print(f"{type_of_bread} bread")

make_sandwich("brown", "bacon", "lettuice", "tomatoes") #if you print this, then it will return None at the bottom of the function output
    #just call the function, and then the result will be printed in this