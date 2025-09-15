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

if __name__ == "__main__":
    """
        -> this is a boolean that says 'only execute this code if the .py file is currently being executed"
        -> if this .py file (module) is being imported into another .py file and executed there, then the __name__ == "__main__" dunder is False 
        -> this means that the section of code in this indentation is not executed, in this case
        -> we separate the .py file into two sections:
            -> the code we want to be executable when this file is ran (inside this __main__ if block) 
            -> the code which we want to be importable into other .py files (outside of this if block)
        -> without this if block, then the code inside it will be executed whenever the .py file (this module) is imported elsewhere
        -> this is the code we don't want to be executed when this .py file (module) is imported elsewhere 
        -> DUNDER REFERS TO SPECIAL METHODS WITH __'S
    """
    #this prints out the value of the potato variable in an f string
    print(prepare(potato)) #cooked potato - WHEN THIS .PY FILE IS RUN
