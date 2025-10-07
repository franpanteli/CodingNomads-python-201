"""VSCode Debugger Watch Tab Video Notes
    -> in the VScode visual debugger
    -> the watch tab
    -> we are getting extra information about the script which we are running
        -> like metadata / in pdb (the Python debugger)
    -> you can add eany Python expression for the debugger to watch
        -> to keep track of what the x+1 expression is supposed to be, for example
        -> THE WATCH TAB IN THE DEBUGGER IS TO WATCH WHAT THE VALUE OF AN EXPRESSION IS SUPPOSED TO BE
    -> he goes to a bug which he deliberatley created in the code and sees the value of this using the watch tab
        -> going to the next breakpoint shows the value of thsi expression
        -> WE ARE ADDING INFORMATION WHICH WE DON'T HAVE IN THE SCRIPT
        -> going to the next round and the value of the watch expression changes
        -> IT IS AN EXPRESSION THAT WE WANT TO WATCH THE VALUE OF
            -> to explore what the script is doing vs what we are expecting it to do
            -> we are not re-assigning x in this case, the value of the variable / expression remains the same
    -> he restarts the debugger session again
        -> not changing the code when the debugger session is running
        -> you can see how the code changes during the running of the debugger session by stopping it and inspecting
            the code again
    -> debugger features <- next
        -> this is using a visual debugger in the IDE
"""

my_list = [11, 22, 3, 5, 42]

new_list = []
for x in my_list:
    x = x + 1
    new_list.append(x)

print(new_list)