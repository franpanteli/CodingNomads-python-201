"""Python Debugger Options Webpage Notes
    -> outline
        -> introduction
        -> colourful CLI debugger with variable inspector
        -> web-based debugger, with clickable user interface
        -> Python debugger options
            -> change the relevant environment variable
    -> Python debugger options
        -> when you use the breakpoint() function in the code, this launches the pdb debugger in the CLI
        -> this is black and white
        -> there are other debuggers, which use colours
            -> pudb <- a more visual CLI-based debugger
            -> web-pdb <- a visual debugger in the web browser, with a clickable UI
        -> this webpage is about these alternatives to pdb
    -> colourful CLI debugger with variable inspector
        -> pdb (Python debugger) was the previous debugger we were using
        -> this is pudb <- a more visual CLI-based debugger
        -> this is a third-party package, which needs installing
            -> python3 -m pip install pudb
            -> this should be done in a virtual environment
        -> we then need to edit the PYTHONBREAKPOINT environment variable, so that Python knows to use this debugger
            and not pdb
        -> we created a virtual environment, activated it, installed pudb and then defined an environment variable
            -> this was defined using export PYTHONBREAKPOINT=pudb.set_trace
            -> this means we are using this debugger in the code
    -> when running the code with this debugger
        -> this is different from the text-based pdb debugger in the previous sessions
        -> you can see all variables and their values
        -> there is a variable inspector at the top RHS of the terminal
        -> this shows the values of all variables the pudb is currently pointing to
        -> this uses the same commands as the pdb inspector
"""

a = 0
b = 42
breakpoint()
a += b
breakpoint()