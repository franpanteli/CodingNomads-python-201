"""What is Python PDB Webpage Notes
    -> outline
        -> introduction
        -> exploring the debugger
            -> debugger practice
        -> summary on what the Python PDB is
    -> Python debugger
"""

#we have this code:
a = 0
b = 42
breakpoint() #setting a breakpoint()
a += b
breakpoint()

"""
    -> when the script is run, this is what shows in the terminal:
        (venv) ➜  python debugging.py
        > /Users/martin/Documents/codingnomads/debugging.py(4)<module>()
        -> a += b
        (Pdb)
    -> this is a debugger session with Python's default debugger, pdb
    -> there is a prompt text to Pdb
    -> this shows we are in the interactive debugging session 
    -> explore the debugger
        -> we can explore the current state of the program 
        -> inspecting the value of variables
        -> interact with them (e.g, to check the datatype of a variable)
    -> debugger practice
        -> the output of print(a) is 0
            -> we are at the first breakpoint 
        -> you can print b as well, this is 42; we are at the first breakpoint 
        -> we can print(b+3) as well 
        -> a is 42 at the second breakpoint, this can be found by commenting out the first one
            -> YOU CAN USE next OR n AND HIT ENTER, FOR THE NEXT PART OF THE CODE EXECUTION
            -> a is 42 at the next breakpoint if this is done  
        -> you can't actually change the values of the variables inside the debugger
        -> it is an interactive debugger
        -> YOU CAN ACTUALLY CHANGE THE VALUES OF VARIABLES IN THE DEBUGGER <- NEXT
        -> interactive debugger session <- next
            -> this includes shortcuts  
    -> summary 
        -> the interactive debugger is to inspect the code, to see potential errors
        -> steps 
            -> we use the breakpoint() function in the code, to declare where its breakpoints are
            -> we execute the code normally and when it hits the breakpoint() function, it starts a debugger session 
                -> this can be used to print out the value of variables 
                -> rather than using the print function, this can be used for all the variables and is better for larger 
                    programs
            -> then explore the values of variables when breakpoint() is initiated
            -> YOU CAN THEM USE next, OR N IN THE CLI TO MOVE ONTO THE NEXT breakpoint() FUNCTION
        -> YOU CAN ONLY GO FORWARD IN THE DEBUGGER 
            -> you can't step backwards 
            -> it only keeps the memory moving forwards
        -> THERE ARE OTHER LIBRARIES TO DEBUG WITH, BUT PDB IS WITH PYTHON'S STANDARD LIBRARY  
"""
