"""VSCode Debugger Controls Video Notes
    -> visual features of the debugger in VSCode
    -> there is a variables tab in the LHS pane
        -> it has the different variables we have defined and their values
        -> it tells us the breakpoint we are at in the code
            -> the margins are lit up different colours for this
        -> he manufactures a bug in the code and restarts the debugger
            -> YOU CAN STEP THROUGH THIS, BY USING THE STEP OVER BUTTON
            -> THERE IS ALSO A STEP THROUGH BUTTON
                -> WE CAN STEP TO THE NEXT LINE, OR TO THE NEXT BREAKPOINT
                -> it shows the updated values of the variables at the next breakpoint
                    -> it shows the ones which have changed since the last breakpoint in a different colour
                    -> we know where the bug is (he created it deliberatley)
                -> THE VARIABLES TAB TELLS US THE VALUES OF THE UPDATED VARIABLES
"""

my_list = [1, 22, 3, 5, 42]

new_list = []
for x in my_list:
    x = x + 1
    new_list.append(x)

print(new_list)