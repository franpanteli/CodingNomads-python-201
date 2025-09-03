text = "hi, earth!"
file_out = open("hello.txt","w") #wirte mode, write to the file
    #this has created the hello.txt file in the same directory as the file
file_out.write(text) #the write method, this has to be a string
    #to see the changes, you have to open and close the same file
