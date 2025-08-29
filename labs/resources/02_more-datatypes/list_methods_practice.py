"""
Practice Using list.remove()
Practice using list.remove() by creating a list a = [1, 2, 3, 2] and then removing the value 2.
What do you notice when you run this code?
Do all occurrences of 2 get removed?
If not, then which 2 has been removed? What direction does list.remove() operate in?
    """

a = [1, 2, 3, 2]
a.remove(2) #this just removes the first occurance of 2 in the list
#the list)name.remove() method moves from left to right in terms of the element removed
print(a)

a = [1, 2, 3, 2]
a.remove(a[1])
a.remove(a[-1])
print(a)