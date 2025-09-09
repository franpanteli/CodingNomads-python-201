# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(input_list):
  # define the function here
  print("The maximum element in the list is:", max(input_list))
  print("The minimum element in the list is:", min(input_list))
  print("The mean element in the list is:", sum(input_list) / len(input_list))
  print("The sum of the elements in the list is:", sum(input_list))
  # pass

# call the function below here
stats(example_list)