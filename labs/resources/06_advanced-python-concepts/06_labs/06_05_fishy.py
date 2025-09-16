# Using a listcomp, create a list from the following tuple that includes
# only words ending with -fish. Tip: Use an `if` statement in the listcomp.

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')
# list = []
# for i in fish_tuple:
#     if i[-4:] == 'fish':
#         list.append(i)
output_list = [i for i in fish_tuple if i[-4:] == 'fish'] #the if statement goes at the end of the list comprehension
print(output_list)