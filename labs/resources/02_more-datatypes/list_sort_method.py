a = [3, 0, 999, 42]
a.sort() #it sets a equal to sorted a
print(a)
a.sort(reverse=True) #sorting the list a from large to small, the default for this with the .sort() method is from small to large
print(a)
# OUTPUT: [0, 3, 42, 999]

#this organises a from small to large numbers

a = ["a", "c", "b"] #sorting this returns none, because there are no numbers
print(a.sort())

