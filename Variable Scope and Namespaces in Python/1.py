""" 

Exercise 1: Local vs Global Scope Instruction:

Define a variable with the same name in both global and local scopes within a function.
Print the variable from inside the function and outside the function,
observing how Python accesses each variable based on its scope (local vs global).

"""
x = 100

def ex_scope():
    x = 50
    print("Inside function (local x):", x)
    
print("Outside function (global x):", x)
ex_scope()
print("Outside function after calling function (global x):", x)