"""Dunder Names Webpage Notes
    -> when importing code from a .py file, if there is code executed inside the .py file which we are importing from, then the outputs from that file will be imported as well
    -> we only want to import certain variables (not the entire output from the .py file)
        -> the .py file is a module
    -> this is why we use the __name__ namespace
        -> you can use this, or you can also remove any code execution from the file (module) we are importing from, that we have defined
        -> if there is already code execution in the module we are importing, we want to use the __name__ namespace
    -> when we import the .py file (module), everything in that .py file is imported
        -> if there are outputs from code execution in that module, then we need to nest them in an if __name__ == "__main__" block in the code
    -> dunder name
        -> this code is added to the bottom of the module (the .py file being imported)
        if __name__ == "__main__":
            # your code execution goes here
            -> this section includes all of the executables which we don't want to import in other modules
            -> this is the same as saying 'if we are in this current .py file, execute these things' (rather than if the code from this .py file is being imported)
    -> there is an example of this in the ingredients.py file
    -> DUNDER IS A METHOD WITH TWO __'S
    -> summary
        -> if __name__ == "__main__:" IS ADDED TO THE BOTTOM OF THE SCRIPT
        -> __ is a dunder method
        -> this is a boolean
        -> the logic inside this block only runs when that .py file (module is ran), NOT WHEN IT IS IMPORTED ELSEWHERE
"""

