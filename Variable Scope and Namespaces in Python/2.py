""" 

Exercise 2: Namespace Exploration Instruction:

1. Create a Python script with two functions, each defining a variable with the same name but with different purposes
(e.g., count variable in a counting function and a logging function).
2. Call both functions and print the variable inside each function, observing how namespaces keep variables separate
within functions

"""

local_var = 0

def local():
    local_var = 1
    print("Inside local(): ", local_var)
    
    def glo():
        local_var = 3
        print("Inside glo(): ", local_var)

    
    glo()

print("Global scope: ", local_var)
local()