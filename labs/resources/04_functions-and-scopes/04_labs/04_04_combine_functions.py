# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
    #we want to combine both of these functions into one
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

#write_letter() function
def write_letter(name="text"):

    # greet function
    def greet(greeting, name):
        sentence = f"{greeting}, {name}! How are you?"
        return sentence

    print(greet(greeting = "Hello", name = name))
    print(greet(greeting = "Goodbye", name = name))

#we are using the greet function inside the write_letter function
#the greet function is the same as from the course materials
#the write_letter function is from the answer to the previous question

print(write_letter(name="John"))