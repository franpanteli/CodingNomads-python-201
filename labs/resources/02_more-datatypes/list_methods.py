"""
    -> using operators on lists
    -> list methods exist, but tuple methods don't because one is immutable and the other isn't
    -> you can pop elements from the list
    """

bucket_list = ["climb Mt. Everest", "eat fruits from a tree that I planted"]

# Add an element
bucket_list.append("sail across the Atlantic ocean")
print(bucket_list)

# Remove an element, using the .pop() method
bucket_list.pop() #THIS RETURNS THE LAST ELEMENT OF THE LIST, WHICH CAN BE ASSIGNED TO A VARIABLE AND CALLED

# print bucket_list again
print(bucket_list)

#this creates a list, and then adds an element to it
#and then sets it equal to it without that last element
#to print out the same list again

"""the list_name.pop() method
    """

bucket_list = ["climb Mt. Everest", "eat fruits from a tree that I planted"] #list
next_task = bucket_list.pop() #this stores the last element of the list - WITHOUT REMOVING IT

print(next_task) #prints last element of list. This is a string
# OUTPUT: "eat fruits from a tree that I planted"
print(bucket_list)
# OUTPUT: ["climb Mt. Everest"]

"""the list_name.remove() method
    """

    #you can enter the content of the item in the list you want to remove:
bucket_list = ["climb Mt. Everest", "eat fruits from a tree that I planted"] #creates a list
bucket_list.remove("climb Mt. Everest") #remove and then the contents of the element in the list which we want to remove
    #it sets the list equal to the list without the element which we just removed
print(bucket_list)
# OUTPUT: ["eat fruits from a tree that I planted"]

    #you can remove the content in the xth element of the list
bucket_list = ["climb Mt. Everest", "eat fruits from a tree that I planted"]
bucket_list.remove(bucket_list[0])
print(bucket_list)
# OUTPUT: ["eat fruits from a tree that I planted"]
        #this is the same thing as before, just using the index of the element rather than its content
