"""changing list elements
    -> they are mutable (their elements are changeable) - and it's the same list
    -> strings are immutable, but the lists that they are in aren't
    -> you are replacing the element of the list, but not the string, because lists are immutable but strings aren't
        -> this gives a descriprive type error if doing so with tuples
        -> this is called item assignment
    """

bucket_list = ["climb Mt. Everest", "eat fruits from a tree"]
bucket_list[1] += " that I planted" #you can use bucket_list +=, or =
print(bucket_list)

"""
    -> aliasing
        -> variables are pointers to values
        -> one variable can point to values
        -> a is the same as b in terms of a list, but they aren't the same object
        -> this is the difference between as is and == statement in terms of operators
        -> it's to do with them pointing to differnt objects in memory
        -> == is called the identity operator
"""

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True - their values are the same
print(a is b)  # False - they are two different object

#but if you define a and b as actually the same thing, then they will be:
b = a
print(a == b)  # True - their values are the same
print(a is b)  # True - one object is based on the other

"""
    -> when they are two separate objects, if the value of one changes then the value of the other doesn't change
    -> they just happened to be two separate lists with the same value
    -> on the other hand, if one is the same as one, then it's based on it - so if the value of the first one changes then so does the value of the second
    -> you are referencing the same objects in the list
        -> if a and b are equal, and the first element of b changes then so will the first element of a, they aren't two separate lists
    -> this is the same as assigning b to a, and is called alliasing
        -> an allias is like a nickname
        -> to alias two lists is to set the variables which store them equal
        -> the list has two different names, so if one of the names is used to change the list then when it is accessed through its other name, the changes to it still would have occured
    -> it's talking about if it refers to the same object, or not
"""