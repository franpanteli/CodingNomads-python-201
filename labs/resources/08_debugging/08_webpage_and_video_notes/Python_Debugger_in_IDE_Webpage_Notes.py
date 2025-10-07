"""Python Debugger in IDE Webpage Notes
    -> outline
        -> introduction
        -> accessing the debugger in VSCode
        -> interacting with VSCode's debugger
        -> summary of the Python debugger in the IDE
    -> IDES INCLUDE INTEGRATED DEBUGGERS
    -> we have just seen pdb / Python debuggers
        -> pdb, pudb and web-pdb (Python debugger)
        -> being familiar with the general idea of an interface that the visual debugger provide
        -> IDE-BASED DEBUGGERS ALLOW US TO DO MORE
            -> we can set breakpoints in a visual way, rather than using the breakpoint() function in the code
            -> this means you don't have to put extra lines in the script
            -> YOU CAN SET BREAKPOINTS IN VSCODE BY CLICKING ON THE MARGIN NEXT TO THE LINE NUMBERS
            -> you can look at on of the integrated debuggers which comes with VSCode
    -> accessing the VSCode debugger
        -> there is a dropdown next to the play symbol on the topRHS corner of the app
            -> then we debug the .py file
        -> you can also use Cmd + Shift + p
            -> access the debug console with the terminal
            -> FOR THE VSCODE IDE DEBUGGER SESSION TO WORK, YOU HAVE TO SET BREAKPOINTS IN THE MARGINS OF THE CODE
            -> the debugger stops execution where the breakpoints are set
        -> in the VSCode debugger, you can
            -> set breakpoints visually
            -> step through execution
            -> inspect all current variable values
        -> you use buttons in the VScode debugger, unlike with the built-in pdb, Python debugger
        -> there is also a variables panel, and how it displays the current variable values
        -> there is also colour highlighting, to show eventual changes
        -> YOU CAN USE THE DEBUGGER BUILT INTO PYTHON (THE pdb, PYTHON DEBUGGER), OR THE DEBUGGER WHICH IS ALREADY IN VSCODE
            -> IN ONE, YOU USE THE breakpoint() FUNCTION IN THE CODE, AND IN THE OTHER BREAKPOINTS ARE SET IN THE SIDE
            -> IF THIS IS USING SOMEONE ELSE'S CODE, IT MEANS THAT THE BREAKPOINTS WILL ONLY EXECUTE THAT ARE ALREADY IN IT, IF THE breakpoint() FUNCTION IS USED (pdb)
    -> summary, Python, debugger in IDE
        -> VSCODE HAS A BUILT-IN DEBUGGER
            -> this works for debugging .py scripts
            -> to use this, you press the dropdown next to the play symbol on the top RHS of the pane and choose 'Debug Python File'
            -> you can visually set breakpoints, by clicking on the side of the editor
            -> the debugger is used to set breakpoints, set through execution, inspect all current variable values, etc
"""

my_list = [1, 22, 3, 5, 42]

new_list = []
for x in my_list:
    x + 1
    new_list.append(x)
    print(new_list)