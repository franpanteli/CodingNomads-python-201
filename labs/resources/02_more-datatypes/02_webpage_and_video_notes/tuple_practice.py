
#Tuple Practice
    #Create a for loop and iterate over one of your tuples. Print out each element.
tuple_example = (1,2,3)
for i in tuple_example:
    print("The value of the element in the tuple this time is: ",i)

    #Create a tuple that is a collection of only str elements. Access the second letter of the second element in your tuple using indexing.
str_tuple = ("one","two","three")
print(str_tuple[2][2])

 #Iterate over your tuple full of strings and print out the last letter of each string only. For this, you'll need to combine iteration and indexing.
for string in str_tuple:
    print(string[-1])