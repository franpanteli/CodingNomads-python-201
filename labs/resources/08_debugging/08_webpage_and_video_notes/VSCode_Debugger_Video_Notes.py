"""VSCode Debugger Video Notes
    -> in the script we are working with, he is using this in VSCode
    -> we want to debug it, using the debugger built into VSCode
    -> THERE IS AN OPTION TO DEBUG THE SCRIPT IN THE IDE, NEXT TO THE BUTTON WHICH CAN BE USED TO RUN THE CODE
    -> IF THERE ARE NO BREAKPOINTS, THEN THE DEBUG CONSOLE WON'T SHOW ANYTHING
        -> it will be a list, and then that will be it
        -> you need to give it instructions on where to stop and debug the code
    -> there is a breakpoint() function which can be used for this
    -> YOU CAN ALSO ADD BREAKPOINTS IN THE IDE, BY CLICKING ON THE LINE YOU WANT IT TO EXECUTE ON
        -> THERE WILL BE A RED DOT HERE
    -> there are other things popping up in the debug window
    -> YOU WANT TO FOCUS ON THE DEBUG PANEL, TO THE LEFT OF THE CODE
    -> there is a list defined at the beginning
        -> you can look at the different list elements
        -> you can also look at the types of these
        -> YOU CAN ALSO CHANGE THE INFORMATION IN THE DEBUGGING SESSION
        -> THERE IS A STOP SYMBOL TO STOP THE DEBUGGER WHEN IT IS BEING RUN
    -> EITHER, YOU CAN USE THE breakpoint() FUNCTION ON A NEW LINE, OR YOU CAN CLICK ON THE LEFT OF THE LINE TO CREATE
        A RED DOT
    -> controls in the visual debugger <- next
"""

my_list = [1, 22, 3, 5, 42]

new_list = []
for x in my_list:
    x = x + 1
    new_list.append(x)

print(new_list)