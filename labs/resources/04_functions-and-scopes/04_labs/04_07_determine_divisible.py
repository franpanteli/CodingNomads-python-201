#TASK
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

#TAKING APART THE TASK
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
DEFINE ONE FUNCTION:
- define a function that determines whether the number is
  divisible by 4 OR 7 and returns a boolean
"""

def divisible_by_four_or_seven(number):
    number = int(number)
    return (number % 4 == 0) or (number % 7 == 0)

"""
DEFINE ANOTHER FUNCTION:
- define a function that determines whether a number is
  divisible by both 4 AND 7 and returns a boolean
"""

def divisible_by_four_and_seven(number):
    number = int(number)
    return (number % 4 == 0) and (number % 7 == 0)

"""
#USING THE FUNCTIONS:
- take in a number from the user between 1 and 1,000,000,000
"""

while True:
    number = input("Enter a number between 1 and 1,000,000,000: ")
    if int(number) > 1 and int(number) < 1000000001:
        break
    else:
        print("That's not in between the range which you were asked for. Try again please.")

"""
- call your functions, passing in the user input as the arguments,
  and set their output equal to new variables
- print your the result variables with descriptive messages
"""

four_or_seven = divisible_by_four_or_seven(number)

if four_or_seven == True:
    print(f"{number} is divisible by four or seven.")
else:
    print(f"{number} is not divisible by four or seven.")

four_and_seven = divisible_by_four_and_seven(number)

if four_and_seven == True:
    print(f"{number} is divisible by four and seven.")
else:
    print(f"{number} is not divisible by four and seven.")
