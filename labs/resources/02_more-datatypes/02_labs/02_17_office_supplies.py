# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

def last_name_length(dictionary):
    return len(dictionary["full_name"].split()[-1])

# Sort using the function
office.sort(key=last_name_length) #the key is the same as a function, this can be a mapping
    #this applies the method to the entire dictionary
    #now the office list will be / is sorted by the surname length

#now we want to return elements in a specific syntax, using f strings
#this will be done by iterating through the dictionaries that are stored by this list
#the shortest surname is now at the bottom of the list
    #sorted list by surname:  [{'full_name': 'Michael Scott', 'item': "world's best boss mug"}, {'full_name': 'Phyllis Lapin', 'item': 'cut flowers'}, {'full_name': 'Pam Beesly', 'item': 'post-its'}, {'full_name': 'Ryan Howard', 'item': 'business cards'}, {'full_name': 'Stanley Hudson', 'item': 'crossword-puzzle'}, {'full_name': 'Kevin Malone', 'item': 'm&ms'}, {'full_name': 'Meredith Palmer', 'item': 'flask'}, {'full_name': 'Angela Martin', 'item': 'cat food'}, {'full_name': 'Kelly Kapoor', 'item': 'People magazine'}, {'full_name': 'Dwight Schrute', 'item': 'pepper spray'}, {'full_name': 'Jim Halpert', 'item': 'phone'}, {'full_name': 'Creed Bratton', 'item': 'mung beans'}, {'full_name': 'Darryl Philbin', 'item': 'forklift'}, {'full_name': 'Oscar Martinez', 'item': 'calculator'}, {'full_name': 'Toby Flenderson', 'item': 'files'}]

#we want this in this syntax:
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

# office = [
#     {"full_name": "Michael Scott", "item": "world's best boss mug"},
#     {"full_name": "Dwight Schrute", "item": "pepper spray"},
#     {"full_name": "Jim Halpert", "item": "phone"},
#     {"full_name": "Pam Beesly", "item": "post-its"},
#     {"full_name": "Ryan Howard", "item": "business cards"},
#     {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
#     {"full_name": "Kevin Malone", "item": "m&ms"},
#     {"full_name": "Meredith Palmer", "item": "flask"},
#     {"full_name": "Angela Martin", "item": "cat food"},
#     {"full_name": "Oscar Martinez", "item": "calculator"},
#     {"full_name": "Phyllis Lapin", "item": "cut flowers"},
#     {"full_name": "Kelly Kapoor", "item": "People magazine"},
#     {"full_name": "Toby Flenderson", "item": "files"},
#     {"full_name": "Creed Bratton", "item": "mung beans"},
#     {"full_name": "Darryl Philbin", "item": "forklift"},
# ]

#this extracts the longest name in the syntax of LASTNAME, Name
    #this is done through a list comprehension
    #iterating through all of the elements in the office list, calculating the length of LASTNAME, Name
    #and then picking the one with the longest name in this list
max_name_length = max(len(d["full_name"].split()[1].upper() + ", " + d["full_name"].split()[0]) for d in office)

for dictionary in office:
    Name = dictionary["full_name"].split()[0]
    LASTNAME = dictionary["full_name"].split()[1].upper()
    Office_supply_item = dictionary["item"]

#we want the output in the syntax of
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item
#this is done using f string mini language and reading the Python documentation for this
    print(f"{LASTNAME}, {Name:<{max_name_length - len(LASTNAME) - 2}}{Office_supply_item}")

    """{Name:<{max_name_length - len(LASTNAME) - 2}} meaning:
            -> this is the first name, followed by a variable amount of spaces
            -> the amount of spaces is a function of the maximum first name and surname in the office list
            -> <: <- this is left align
            -> - len(LASTNAME) <- this is the length of the longest name in the list
            -> -2 <- we are taking two away, because of a space and a comma
    """