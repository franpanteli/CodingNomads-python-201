# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input = input("Please enter a string: ")
# user_input = "hello" #for testing

keys = list(set(user_input)) #the dictionary keys are each individual character that occurs in the input string,
                                #without duplication. This is converted into a list so that a list of values can
                                #be created and zipped with this, producing the output dictionary

#we want the length of values to equal the length of keys, because we want to zip them to make the output dictionary
#iterate through the keys to calculate the frequency of each character in the user input
values = []
for key in keys:
    character_frequency = 0
    for char in user_input:
        if key == char:
            character_frequency += 1
    values.append(character_frequency)

#zip the keys and values together to create a dictionary n
n = dict(zip(keys, values))

#print the result
print("result =", n)
