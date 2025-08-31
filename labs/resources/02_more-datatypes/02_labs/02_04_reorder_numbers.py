# Read in 10 numbers from the user.
number_one = input("Enter a first number: ")
number_two = input("Enter a second number: ")
number_three = input("Enter a third number: ")
number_four = input("Enter a fourth number: ")
number_five = input("Enter a fifth number: ")
number_six = input("Enter a sixth number: ")
number_seven = input("Enter a seventh number: ")
number_eight = input("Enter a eighth number: ")
number_nine = input("Enter a ninth number: ")
number_ten = input("Enter a tenth number: ")

# Place all 10 numbers into an list in the order they were received.
list = [
    number_one, number_two, number_three, number_four,
    number_five, number_six, number_seven, number_eight,
    number_nine, number_ten
]

# Print out the second number received, followed by the 4th,
print("Second number received: ", number_two)
print("Fourth number received: ", number_four)

# then the 6th, then the 8th, then the 10th.
print("Sixth number received: ", number_six)
print("Eigth number received: ", number_eight)
print("Tenth number received: ", number_ten)

# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
print("Ninth number received: ", number_nine)
print("Seventh number received: ", number_seven)
print("Fifth number received: ", number_five)
print("Third number received: ", number_three)
print("First number received: ", number_one)

all_together_list = [number_two, number_four, number_six, number_eight, number_ten, number_nine, number_seven, number_five, number_three, number_one]
print("All together: ", all_together_list)

# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

