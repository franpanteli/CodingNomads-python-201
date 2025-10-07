"""Python Debugger Options Webpage Notes
    -> this is the second virtual environment in these notes
    -> this time, we are using a web-based debugger, not a colourful one in the terminal
    -> there is a colourful one in the terminal, this one, and one which is native to Python
        -> this is the Python debugger (pdb)
    -> we are using a virtual environment, so that the debugger being used is local to that environment, and not
        system-wide
    -> web-pdb
        -> web based Python debugger
        -> we can access the debugger in the browser and click buttons, instead of typing shortcuts
        -> we set the PYTHONBREAKPOINT environment variable in the CLI
            -> export PYTHONBREAKPOINT=web_pdb.set_trace
            -> this is so the virtual environment knows to use the webpage debugger
        -> we then run thus script from inside that terminal, with Python3
        -> the console shows the time that the debugger session started
        -> shows, we go to the following url: http://localhost:5555/
        -> the debugger session has started in this
        -> this shows an environment like a Jupyter notebook, for debugging the code
            -> it is interactive
            -> it looks like multiple screenshots in the browser, but they are interactive
            -> once the variables have been clicked through, the debugging session needs to be restarted in the CLI
        -> this shows the debugger interface
        -> there is a variable inspector on the top right of the interface
            -> this looks similar to the pudb debugger, except buttons in the browser can be used in the debugger
                session
            -> THERE IS DOCUMENTATION FOR EACH OF THESE DEBUGGERS
"""

a = 0
b = 42
breakpoint()
a += b
breakpoint()

"""Summary 
    -> the default debugger is the pdb, the Python debugger
        -> this is in the standard library 
    -> you can also install two other types of debugger, to make the experience more visual 
        -> the first is in the CLI, the second is in the browser 
    -> THE PYTHONBREAKPOINT ENVIRONMENT VARIABLE HAS TO BE CHANGED IF YOU WANT TO USE A DIFFERENT DEBUGGER, IN A VIRTUAL 
        ENVIRONMENT  
        -> we can debug with different tools in different environments
        -> to use a debugger with a GUI on the local development machine 
            -> you can also use a plain text one one the server, without needing to change the code
    -> the relevant environment variable is changed by using: export PYTHONBREAKPOINT=web_pdb.set_trace
        -> this tells the virtual environment to use the web_pdb debugger, instead of the default pdb
        -> this debugger will be used when the new debugger session starts    
"""