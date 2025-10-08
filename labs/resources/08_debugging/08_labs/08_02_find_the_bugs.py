# The code below contains a few bugs. Use your debugger to find and fix them.

"""
    -> we want to use a debugger to get rid of the bugs in this code
    -> it has not specified what the code is supposed to do
    -> the easiest thing is to use the breakpoint() function throughout the cpde, and then run a debugging session in
        the terminal
    -> we can use the other debuggers, pudb and web-pdb, or the debugger built-into the IDE
        -> pdb is the Python debugger (using the breakpoint() function in the code and then running the debugging
            session in the CLI, by just running the code
        -> pudb is an external library which is installed, in a virtual environment
            -> we want to use the pdb debugger, because it's the only of the three that doesn't require installing
                a third-party library
            -> and then the pudb debugger is the Python Urwid Debugger (it is based on the Urwid library)
                -> this requires installing with a third party in the CLI
                -> when this debugger is run, there is an animation / prettier looking interface in the CLI
                -> the debugger session is run by playing the code
                -> the debugger still requires breakpoint() functions
            -> the other debugger is the web-pdb debugger
                -> this is one which requires third-party installation
                -> we execute the code, with the breakpoint() function used, in the CLI
                    -> and then, we go to a certain URL (in the course notes), and the debugger session is executing
        -> THE EASIEST DEBUGGER TO USE FOR THIS EXERCISE IS THE ONE BUILT INTO THE IDE
            -> this IDE is PyCharm
            -> we want to use the debugger in it
            -> it might also be easier to use the built-in pdb debugger, with the breakpoint() function in the code
                -> this is considering that we then have to work out how to use the PyCharm debugger
                    -> to set breakpoints in this debugger, we click on the left margin of certain lines of code
                        and then they show up red
                        -> this means that a breakpoint has been set
                    -> then we click on the debugger symbol next to the play button on the top RHS IDE pane
    -> working out what the code does
        -> we have an unsorted list
        -> we want to sort the list
        -> it's a list of tuples
        -> so we are first defining a list of tuples
        -> we want to debug it using a debugger; would rather use the breakpoint() funciton
        -> if the code is this bad (with three issues like this), then the best solution is just to write the
            entire thing again, rather than debug it
            -> to go back to paper and write it out more carefully
"""

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)] #define the list we want to sort
sorted_list = [] #initialise the list we want to populate

"""
    -> when we run the code, it tells us which line the error is on
    -> I would normally use print statements, and not the debugger for this
"""

while unsorted_list: #iterating through the unsorted list

    """
        -> the above line used to be for x in range(1, len(unsorted_list)):
        -> this was changed to a while loop, because we want to loop through all the list elements
        -> the previous solution was only sorting two list elements (not three)
        -> we are removing the next minimum element from the unsorted list and appending it to the new list
            -> using a while loop for this means we carry on, until there are no more elements in the original 
                list left  
    """

    minimum = unsorted_list[0][1] #set the minimum element to 'first_element' in the unsorted list
        #THE ISSUE IS THAT THE LINE ABOVE SAID THIS: minimum = unsorted_list[0][0]
        #CHANGING IT TO minimum = unsorted_list[0][1] OUTPUTS THE SORTED LIST AS
        # [('first_element', 4), ('second_element', 2), ('third_element', 6)]

    index = 0 #initialise the index as 0

    """
        -> we have another iterable list 
            -> we are iterating through all of the elements in the unsorted list 
            -> they have deliberatley given us code which doesn't work 
    """

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i][1] < minimum: #this is the condition for the new minimum; if it is met, the element we are
                                            #iterating through is a minimum
            minimum = unsorted_list[i][1] #storing the new minimum
                #THIS LINES USED TO BE minimum = unsorted_list[i][i] - the last i was changed to a 1
                #this was so that the function would set the minimum as a number (the syntax of the list elements is a
                #string and then a number - this sets the minimum as the last element in one of the tuples (a number)
            index = i #the index of the minimum
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])

print(sorted_list)
