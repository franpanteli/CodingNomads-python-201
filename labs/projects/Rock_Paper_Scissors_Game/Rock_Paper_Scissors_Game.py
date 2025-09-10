"""
# Rock-Paper-Scissors Game

Code a game of rock paper scissors.

## Instructions

* take in a number 0-2 from the user that represents their hand
* generate a random number 0-2 to use for the computer's hand
* call the function `get_hand` to get the string representation of the user's hand
* call the function `get_hand` to get the string representation of the computer's hand
* call the function `determine_winner` to figure out who won
* print out the player hand and computer hand
* print out the winner

## Some Tips

Creating a function that gets a "hand" based on a number.

The function should take in a number and return the string representation of the hand. E.g.:

```python
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper

    # for example if the variable hand is 0, it should return the string "scissor"
    pass
```
    """

#import random module
import random

def get_hand(): #this function asks the user for a number and outputs the number as a string

    user_input = input("Enter a number between 0-2, this will represent your hand: ")
    # 0 = scissor, 1 = rock, 2 = paper
    if int(user_input) == 0:
        user_output = "scissor"

    if int(user_input) == 1:
        user_output = "rock"

    if int(user_input) == 2:
        user_output = "paper"

    computer_hand = random.randint(0, 2)

    if computer_hand == 0:
        computer_output = "scissor"

    if computer_hand == 1:
        computer_output = "rock"

    if computer_hand == 2:
        computer_output = "paper"

    return user_output, computer_output #example output ('paper', 'paper'), the output of this function is a tuple

def determine_winner():

    tuple = get_hand()
    user_output = tuple[0]
    computer_output = tuple[1]

    #initialise booleans
    user_wins = False
    tie = False

    #when the user wins
    if (user_output == "rock") and (computer_output == "scissor"):
        print(f"The user wins. The user guessed {user_output} and the computer guessed {computer_output}.")
        user_wins = True

    if (user_output == "paper") and (computer_output == "rock"):
        print(f"The user wins. The user guessed {user_output} and the computer guessed {computer_output}.")
        user_wins = True

    if (user_output == "scissor") and (computer_output == "paper"):
        print(f"The user wins. The user guessed {user_output} and the computer guessed {computer_output}.")
        user_wins = True

    #tie cases
    if user_output == computer_output:
        print(f"Tie! The user and computer both guessed {user_output}.")
        tie = True

    if (user_wins == False) and (tie == False):
        print(f"The user looses. You guessed {user_output} and the computer guessed {computer_output}.")

determine_winner()
