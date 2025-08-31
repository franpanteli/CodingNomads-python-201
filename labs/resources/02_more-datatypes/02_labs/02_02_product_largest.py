#import modules
# this doesn't work, but you can see it's trying to import from the resources folder in the project files
    # import resources
    # from resources import randlist
import random
randlist = [random.randint(0, 100) for _ in range(10)]

# Take in a few numbers from the user and place them in a list.
# number_one = input("Give me a number: ")
# number_two = input("Give me another number: ")
# number_three = input("Give me a third number: ")
# list_of_numbers =[number_one, number_two, number_three]
# print(f"This is a list of those numbers: {list_of_numbers}")

# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
print("randlist: ", randlist)

# Find the largest number in the list and print the result.
print("The largest number in randlist is: ", max(randlist)) #not randlist.max(), or randlist.maximum(), because there
    #is no possible argument for this (it's just a number)
    #max is a function, not a number

# Calculate the product of all of the numbers in the list.
product = 1
for i in randlist:
    product = product*i
print("The product of all the numbers in the list is: ",product)









