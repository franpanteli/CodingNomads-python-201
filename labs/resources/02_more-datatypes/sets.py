"""Sets
    -> they are mutable, so functions can operate on them
    -> unordered collections with no duplicates
    -> {} syntax
    """
s1 = {1, 2, 3} #this is a set
print(s1) #prints out the set
# OUTPUT: {1, 2, 3}

s2 = set([1, 2, 3]) #converts a list into a set
print(s2) #prints it
# OUTPUT: {1, 2, 3}

s3 = set() #makes an empty set
    #USING {} CREATES AN EMPTY DICTIONARY, NOT AN EMPTY SET
print(s3) #prints the empty set
# OUTPUT: {}

"""TO GET RID OF DUPLICATES IN A LIST, CONVERT THE LIST INTO A SET
    -> A SETOF THINGS DON'T CONTAIN DUPLICATES
    -> YOU CAN TAKE A LIST AND CONVERT IT INTO A SET, TO GET RID OF THE DUPLICATES
"""

url_list = ['http://www.example.com',
'http://www.setsareuseful.com',
'http://www.example.com']#thisis a list which contains three urls, and two of them are the same

unique_urls = set(url_list) #converting that list into a set (a set of things / items) removes the duplicates
print(unique_urls)
# OUTPUT: {'http://www.example.com', 'http://www.setsareuseful.com'}
