courses = ['Intro', 'Intermediate', 'Advanced', 'Professional'] #list of courses

for index, course in enumerate(courses): #the index and the element in the list
    print(f"{index}: {course} Python")

# OUTPUT:
# 0: Intro Python
# 1: Intermediate Python
# 2: Advanced Python
# 3: Professional Python

#you create a for loop, where we want an index and a value
"""the enumerate() function
        -> it's a tuple containing an index and a value

(0, 'Intro')
(1, 'Intermediate')
(2, 'Advanced')
(3, 'Professional')

        -> this can use tuple unpacking
        ->
    """