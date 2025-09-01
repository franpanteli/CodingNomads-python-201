# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

#THE USER ENTERS SOMETHING
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

list_of_integers = [] #initialise list of integers
points = 5 #initialise points; the lowest this can go is 0
print("Please note that you can enter exit(), to exit the game at any point.")

while True: #an infinite loop asking for user input
    user_input = input("Please enter an integer: ") #ask for user input, this is always a string

    if user_input == "exit()": #exit the program if the user types exit(), this is easier than ctrl c
        break

    try: #try converting it into an integer
        user_input = int(user_input)
        """
    -> if what the user entered can't be converted into an integer, this returns an error message straight away
    -> this is ValueError
    -> if it can be converted into an integer, then this is stored in the integer value
        """

#THE USER HAS ENTERED AN INTEGER, user_input
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#sets are immutable, and we want to add user_input to a set
#we first add it to a list, and calculate the length of the list
#then convert the list into a set, in which case the duplicates will be removed
#if the length of the set isn't equal to the length of the list, then we deduct a point (-1)

        list_of_integers.append(user_input) #add the user input to the list of integers
        if len(list_of_integers) != len(set(list_of_integers)):

            #\puts the f string literal on a new line in the IDE
            print(f"That input is a duplicate, now you get a point deducted. You have {points} points remaining.")
            points -= 1 #take away 1 from points

            #exit the program if the user looses 5 points:
            if points <= 0:
                print("You lost 5 points, you lost the game. Goodbye!")
                break

        #if the user enters 10 unique numbers, they win the game
        if len(set(list_of_integers)) >= 10:
            print("You win the game, because you managed to create a set that has more than 10 integers!")

#THE USER HAS NOT ENTERED AN INTEGER
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    except ValueError: #in the case that what the user enters can't be converted into an integer
        print("That's not an integer, try again.")