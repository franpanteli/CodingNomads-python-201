"""VSCode Debugger Recap Video Notes
    -> the visual debugger inside VSCode and interacting with it
    -> we can create breakpoints, by clicking on the margin or using the breakpoint() function in the code
    -> we can run the debugger in the IDE, by clicking the button next to the play one on the top RHS of the screen
        (in full screen)
    -> in the debugger pane on the left
        -> this is during a debugging session
        -> we can see variables and the watch tab
        -> this changes WHEN WE STEP THROUGH THE SCRIPT
        -> THE WATCH TAB CAN BE USED TO TRACK THE VALUES OF CERTAIN EXPRESSIONS AS THE CODE IS EXECUTED
        -> we also have the step over function
            -> WE CAN MOVE ONTO THE NEXT LINE IN THE CODE, AND ALSO THE NEXT BREAKPOINT
            -> the step over function <- line by line in the script
    -> step into and step out <- to step into and out of the function
    -> these are the action buttons in the debugger
    -> this is the debugger tool in the IDE
        -> to debug the script more visually
"""

my_list = [1, 22, 3, 5, 42]

new_list = []
for x in my_list:
    x = x + 1
    new_list.append(x)

print (new_list)