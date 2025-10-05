"""Python Breakpoint Webpage Notes
    -> outline
        -> introduction
        -> the breakpoint function
        -> older Python versions
    -> introduction
        -> breakpoint is a flag which allows us to inspect the script where the breakpoint is
        -> it is like when defining a document, we can introduce breakpoints
        -> THIS IS A POINT IN THE CODE WHERE WE CARE ABOUT KNOWING WHAT THE VALUES OF VARIABLES ARE
    -> the breakpoint() function
        -> the breakpoint() function
        -> this allows us to access a debugger in the IDE
        -> THIS IS USED IN DEBUGGING SESSIONS
        -> to inspect the value of all the variables in the scirpt
            -> we can see what the kernel stores
            -> you can interact with the variables as well
            -> it's like a print statement, on all the variables in the code
        -> IT IS A FUNCTION WHICH IS CALLED IN THE CODE
            -> WHEN THE IDE HITS THE BREAKPOINT() FUNCTION, IT STARTS EXECUTING A DEBUGGER SESSION; PRINTING OUT THE
                VALUES OF ALL THE VARIABLES UP UNTIL THAT POINT
            -> this starts the interactive debugging session with pdf, Python's debugger in the standard library
                -> PDB IS PYTHON'S STANDARD DEBUGGER IN THE LIBRARY
"""

a = 0
b = 42
breakpoint()
a += b
breakpoint()

"""
    -> Python versions older than 3.7
        -> the breakpoint() function won't work 
        -> you would have to use pdb.set_trace() where you would want to start the debugger
        -> this is what the same code would look like in an older version:
            a = 0
            b = 42
            import pdb; pdb.set_trace()
            a += b
            pdb.set_trace()
        -> this is less intuitive than breakpoint()
            -> it also requires a module import 
        -> how to interact with the debugger <- next
            -> this starts running in the CLI, when it hits the breakpoint() function 
"""