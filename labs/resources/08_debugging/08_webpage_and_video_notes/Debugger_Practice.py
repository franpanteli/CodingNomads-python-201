a = 0
b = 42
breakpoint()
a += b
breakpoint()

"""
>(venv) **➜ ****debugging** Python -m pdb debugging.py
> /Users/martin/<YOUR_PATH>/debugging.py(1)<module>()
-> a = 0 
(Pdb) p a #PRINT THE VALUE OF a
*** NameError: name 'a' is not defined
(Pdb) n
> /Users/martin/<YOUR_PATH>/debugging.py(2)<module>()
-> b = 42
(Pdb) p a 
0
(Pdb) p b #PRINT THE VALUE OF b
*** NameError: name 'b' is not defined
(Pdb) n
> /Users/martin/<YOUR_PATH>/debugging.py(4)<module>()
-> a += b
(Pdb) p b
42
(Pdb) n #GO TO THE NEXT BREAKPOINT 
--Return--
> /Users/martin/<YOUR_PATH>/debugging.py(4)<module>()->None
-> a += b
(Pdb) p a
42
(Pdb) p b
42
(Pdb) !a = 100 #UPDATE THE VALUE OF THE a VARIABLE TO 100 
(Pdb) p a #PRINT THE NEW VALUE OF THE a VARIABLE, WHICH WE JUST UPDATED 
100
(Pdb) p b
42
(Pdb) q #QUIT THE DEBUGGER 
(venv) **➜ ****debugging
"""