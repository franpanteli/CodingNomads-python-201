import ingredients as i #this is an alias (import something as something else)
import recipes.soup as s #the soup.py file in the recipies file
    #soup is taken as an attribute of the recipies directory
    #this is accessed via the . method

c = i.carrot #the carrot variable in the ingredients.py file
s.make_soup(c)
"""
    -> is is the soup.py file in the recipies directory 
    -> accessing the make_soup function in this file 
    -> feeding in the value of the carrot variable into the function in the other file, as its argument 
"""