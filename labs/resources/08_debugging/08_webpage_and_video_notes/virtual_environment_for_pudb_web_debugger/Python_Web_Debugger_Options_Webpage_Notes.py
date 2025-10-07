"""Python Debugger Options Webpage Notes
    -> this is the second virtual environment in these notes
    -> this time, we are using a web-based debugger, not a colourful one in the terminal
    -> there is a colourful one in the terminal, this one, and one which is native to Python
        -> this is the Python debugger (pdb)
    -> we are using a virtual environment, so that the debugger being used is local to that environment, and not
        system-wide
    ->
"""

a = 0
b = 42
breakpoint()
a += b
breakpoint()