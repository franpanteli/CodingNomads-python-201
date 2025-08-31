users = {'mary': 22, 'caroline': 99, 'harry': 20}

#Change the age of "caroline" from 99 to 26
users['caroline'] = 26
# print(users)

#Use the code playground below to age each user for 10 years
users['mary'] = 10
users['caroline'] = 10
users['harry'] = 10
# print(users)

#Play around with the code and add or delete some dictionary entries. How does that affect your output?
users['john'] = 10 #this key-value pair did not previously exist in the dictionary
print(users)
del users["john"] #this removes the john key-value pair from the dictionary
print(users)
