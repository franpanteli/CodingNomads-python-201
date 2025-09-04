"""
    -> the Python path 
        -> doing something like this:
        with open("input.txt", "r") as file_in:
        print(file_in.read())
            assumes that the file is in the same path as the folder which contains the .py file
            -> we want to use relative paths 
    -> paths you can use
        -> the relative path is from the .py file to the file we want to create
        -> the absolute paths is the absolute path of the file on the system we want to create
            -> e.g with open("/Users/yourname/Desktop/input.txt", "r") as file_in:
                    print(file_in.read())
            -> the issue with this is that it changes depending on the operating system 
            -> one way around this is with the pathlib module
"""

# with open("input.txt", "r") as file_in: #this is a context manager
#     print(file_in.read())

from pathlib import Path #using this module works independently of the operating system 

data_path = Path("/Users/francescapanteli/Desktop") #you can save the path in a variable 

with open(data_path.joinpath("input.txt"), "r") as file_in: 
    """data_path is then used in the context manager
        -> the open method is then used 
        -> namelly, this would be open (file of the file, read/append/write mode)
        -> this is open(name_of_absolute_path.joinpath(filename, read/append/write))
    """
    print(file_in.read())

#a faster way of doing this:
from pathlib import Path #import module

filepath = Path("/Users/yourname/Desktop/input.txt") #store the path to the file, and the filename in a variable 

with filepath.open() as f: #use a context manager to open it
        #this is with the open method and the file_path.open()
    print(f.read()) #printing the filename 

"""
    -> path methods     
        -> you can build something which reads from and writes to files
        -> the next section of the course is on functions 
        -> import the path class
            -> file system paths as objects
            -> each path object contains a path in the form of a string 
    -> the location of the file can be chosen as relative or absolute
        -> from the root directory, or the location of the .py file
        -> the pathlib file is independent of the operating system being used 
"""

from pathlib import Path

p = Path("hello.txt") #the path to this file 
    #the hello.txt file in the current working directory 
p.write_text("Hello world!") #write text to the file stored at this directory 
    #writes "Hello world!" into the file 
p.read_text()  # OUTPUT: "Hello world!" <- output the contents of the file 
    #opens the file, reads the content and returns it as a Python string 
    #this does it without the open() function 

