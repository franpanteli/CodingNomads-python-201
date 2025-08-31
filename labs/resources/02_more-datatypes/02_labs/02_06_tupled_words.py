# Write a script that takes a string from the user
string = input("Give me an input string: ")
# string = "hello world" #test string

# and creates a list that contains a tuple for each word.
# For example:
# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

list_of_words = string.split()
#use a list comprehension:
result_list = [tuple(list(i)) for i in list_of_words]
print(result_list)



