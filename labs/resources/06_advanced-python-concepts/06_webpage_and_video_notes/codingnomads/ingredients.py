# ingredients.py
    #this defines a function which prints out the ingredient
def prepare(ingredient):
    return f"cooked {ingredient}"

#these are variables which can be imported in other modules (.py files)
    #this can be done in a venv (virtual environment)
carrot = "carrot"
# carrot = "Hello, world!"
salt = "salt"
potato = "potato"

#this prints out the value of the potato variable in an f string
print(prepare(potato)) #cooked potato
