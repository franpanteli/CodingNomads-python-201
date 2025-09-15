"""Import Namespaces Webpage Notes
    -> if we want to import code from a .py file, which is inside another directory
    -> side effects from importing
        -> when a variable from one script is imported into another script, the entire script importing the variable in is ran
        -> even though you just want to import one variable, the entire .py script gets imported
        -> next <- ways around this
    -> summary
        -> when importing Python from a module (a .py file), Python executes the entire script
        -> leftover function calls are also executed <- code which we don't want to execute, for example if we only want one variable
"""