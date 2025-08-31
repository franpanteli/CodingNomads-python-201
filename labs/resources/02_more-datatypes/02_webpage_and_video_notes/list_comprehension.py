names = ["Ada", "Bertha", "Carol"] #list of names
    #this syntax is list comprehension - it's defining a new list using syntax which is backwards to regular for loops, for i in is at the end
    #we can do this because lists are mutable and tuples aren't
lowercase_names = [x.lower() for x in names] ## OUTPUT: ['ada', 'bertha', 'carol']
    #this is another list, it's in square brackets
    #this is like for i in:, except the for i bart comes afterwards (it's backwards)

#ANOTHER WAY OF DOING THIS
lowercase_names = [] #define the empty list
for x in names: #iterate through the elements of the list
    lowercase_names.append(x.lower()) #make them lowercase and add that to the empty list (this can be done in one line)

print(lowercase_names)
# OUTPUT: ['ada', 'bertha', 'carol']

#comprehensions also exist
