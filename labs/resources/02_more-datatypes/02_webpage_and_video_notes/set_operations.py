"""USING SET OPERATIONS
    -> this is like maths
    -> sets can be iterated through

A | B	A.union(B)	Returns a new set that contains all elements of A and B.
A |= B	A.update(B)	Adds all elements of B to the set A.
A & B	A.intersection(B)	Returns a new set that contains the elements that are in both A and B.
A - B	A.difference(B)	Returns the elements that are included in A but not included in B.
A -= B	A.difference_update(B)	Removes all elements of B from the set A.
A < B		Equivalent to A <= B and A != B
A > B		Equivalent to A >= B and A != B

-> next is dictionaries
->SETS ARE USED TO REMOVE DUPLICATES FROM COLLECTIONS, AND ARE MUTABLE LIKE MATHEMATICAL SETS
"""

#USING THE .UNION() METHOD FOR SETS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#we are using the .union and .update methods on sets
set_one = {1,2,3} #none of these elements are repeated
set_two = {4,5,6}

print("set_one.union(set_two): ", set_one.union(set_two))
print("set_two.union(set_one): ", set_two.union(set_one))
#the resukt of this in both cases is another set

#USING THE .UPDATE() METHOD FOR SETS
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# A.update(B) Adds all elements of B to the set A.
#this is the same as saying set A equals set A plus set B
#it doesn't change set B

set_one.update(set_two) #this adds set two to set one and sets set one equal to this
set_two.update(set_one) #this adds set one to set two and sets set two equal to this

print("set_one.update(set_two): ", set_one.update(set_two)) #None
print("set_two.update(set_one): ", set_two.update(set_one)) #None

print("set_one.update(set_two): ", set_one) #this prints out set one after set two has been added to it
print("set_two.update(set_one): ", set_two) #this prints out set two after set one has been added to it