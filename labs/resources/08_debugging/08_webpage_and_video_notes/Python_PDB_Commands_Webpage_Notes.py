"""Python PDB Commands Webpage Notes
    -> outline
        -> introduction
        -> most common PDB commands
            -> practice with the commands
        -> summary of Python PDB commands
            -> most important shortcut commands
    -> outline
        -> you need to use the debugger a lot to understand it
        -> this session is on the most important commands in pdb
        -> then we have an example debugger session in the code snippet from earlier
    -> most common PDB commands
        -> shortcuts in a PDB session
            -> n <- next; move to the next breakpoint
            -> c <- continue; carry on until another breakpoint
            -> p <- print
            -> pp <- pretty-print the variable's value
            -> !<expr> <- execute Python statements as if in a normal interpreter session
            -> q <- exit the Python debugger
        -> these commands need practicing in the pdb debugger
    -> practice with debugger commands
        -> we want to explain what happens at each step of the debugger

            >(venv) **➜ ****debugging** Python -m pdb debugging.py
            > /Users/martin/<YOUR_PATH>/debugging.py(1)<module>()
            -> a = 0
            (Pdb) p a
            *** NameError: name 'a' is not defined
            (Pdb) n
            > /Users/martin/<YOUR_PATH>/debugging.py(2)<module>()
            -> b = 42
            (Pdb) p a
            0
            (Pdb) p b
            *** NameError: name 'b' is not defined
            (Pdb) n
            > /Users/martin/<YOUR_PATH>/debugging.py(4)<module>()
            -> a += b
            (Pdb) p b
            42
            (Pdb) n
            --Return--
            > /Users/martin/<YOUR_PATH>/debugging.py(4)<module>()->None
            -> a += b
            (Pdb) p a
            42
            (Pdb) p b
            42
            (Pdb) !a = 100
            (Pdb) p a
            100
            (Pdb) p b
            42
            (Pdb) q
            (venv) **➜ ****debugging

        -> we are running the example in the interactive debugger
        -> pdb COMMANDS HAVE DOCUMENTATION
            -> there are other commands, which may be useful
            -> writing it out manually on a piece of paper, adding comments and explanations
            -> like a web design wire frame
            -> writing out by hand can help with memorising it
        -> future lesson
            -> other interactive debuggers for Python
            -> MOST OTHER INTERACTIVE DEBUGGERS FOR PYTHON ARE BUILT ON TOP OF PDB, THE PYTHON DEBUGGER
                -> they try and make the CLi look nicer when the debugging session is running
    -> summary
        -> when the code execution hits a breakpoint() function, the debugger session is initiated in the CLI
        -> we can interact with the state of the script in the CLI
        -> example commands for debugging sessions
            -> n <- execute the current line of code and move onto the next time the breakpoint() function is used inside it
            -> p <- to print the value of a variable
            -> c <- to execute until a breakpoint is encountered (continue)
            -> !<expr> <- to execute Python statements as if in a normal interpreter session
            -> q <- to quit the debugger
        -> these can be used to debug the code, without using multiple print() statements throughout it
"""
