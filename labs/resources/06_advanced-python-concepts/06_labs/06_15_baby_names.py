# You're about to adopt a baby and you don't have a name yet. 😱
# You and your partner agree that the name should start with an 'M',
# but that's about all you've got so far.
#
# To save the day, use the filter() method and a lambda expression
# to map all the baby names that begin with a 'M' to an output list.

names = ['Olivia', 'Noah', 'Ava', 'Oliver', 'Isabella', 'Mason', 'Sophia', 'Logan', 'Emma', 'Liam', 'Amelia', 'Lucas', 'Mia', 'Elijah', 'Charlotte', 'Ethan', 'Harper', 'James', 'Mila', 'Aiden', 'Aria', 'Carter', 'Ella', 'Jackson', 'Evelyn', 'Alexander', 'Avery', 'Sebastian', 'Abigail', 'Michael', 'Emily', 'Benjamin', 'Luna', 'Jacob', 'Riley', 'William', 'Scarlett', 'Grayson', 'Chloe', 'Jack', 'Sofia', 'Daniel', 'Layla', 'Owen', 'Lily', 'Luke', 'Madison', 'Henry', 'Ellie', 'Wyatt', 'Zoey', 'Jayden', 'Elizabeth', 'Leo', 'Penelope', 'Gabriel', 'Victoria', 'Julian', 'Grace', 'Matthew', 'Nora', 'David', 'Aubrey', 'Jaxon', 'Camila', 'Levi', 'Hannah', 'Mateo', 'Bella', 'Asher', 'Aurora', 'Lincoln', 'Addison', 'John', 'Stella', 'Samuel', 'Skylar', 'Muhammad', 'Paisley', 'Ryan', 'Savannah', 'Adam', 'Maya', 'Isaac', 'Natalie', 'Nathan', 'Elena', 'Josiah', 'Emilia', 'Isaiah', 'Violet', 'Joseph', 'Hazel', 'Caleb', 'Nova', 'Anthony', 'Niamey', 'Hunter', 'Eva', 'Eli']
# filter(names, key = lambda x: x.startswith[0])

print(list(filter(lambda x: x[0]=="M", names)))

"""
    -> we are printing out the result (first method)
    -> converting the generator object into a list (second method)
    -> the third method is the filter method 
        -> the arguments of this are the list of names we want to sort (last, `names`)
        -> the first argument of this is the lambda function which we want to sort the elements by 
            -> it is a function, of x in the list
            -> x represents the name in the list
            -> it has to return as a True statement 
            -> the condition for which the function returns as True 
            -> without x in front of the lambda function, then whatever is entered after the colon is returned by the function 
            -> this can be returned if the function is stored in a variable 
                -> but they are still called anonymous functions, because the def keyword with the name of the function isn't used 
"""

#example from webpage
# squares = list(filter(lambda x: x**2, range(10))) #replace the map method with the filter method
# print(squares)
