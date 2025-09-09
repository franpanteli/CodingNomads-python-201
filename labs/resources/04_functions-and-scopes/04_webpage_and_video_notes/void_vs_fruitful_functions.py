# VOID FUNCTIONS
# all function below are void.
# try printing the output of their function calls

def void_func_1(message): #void functions don't return anything
  print(message)

def void_func_2(message):
  print(message)
  return None #void functions return None

def void_func_3(message):
  print(message)
  return

res_1, res_2, res_3 = void_func_1('hi'), void_func_2('hei'), void_func_3('ho')
    #YOU CAN LIST DIFFERENT FUNCTION CALLS IN A TUPLE
print("void returning:", res_1, res_2, res_3)

# FRUITFUL FUNCTIONS
# adding a value to the return statement makes a
# function "fruitful" - it gives it a value that can be worked forward with

def fruitful_func(message):
  # print(message)  # whether or not this is here,
  # the function call produces a value
  return message

f_res = fruitful_func('yay')
print("fruitful returning:", f_res) #the output of the function is accessed by printing it
    #it's a fruitful function, because it returns something
    
