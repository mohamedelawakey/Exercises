""" 

Exercise 3: Scope Hierarchy Instructions: * Define a variable in the global scope, then create a function
with an enclosing scope that redefines a variable with the same name. * Inside this function, access both
the global and enclosing variables and print their values. * Discuss with comments in the code how Python
follows the LEGB rule for variable lookup.

"""

# Global variable
count = 10 

def outer_function():
    # Local variable within outer_function
    count = 20 
    
    def inner_function():
        # Local variable within inner_function
        count = 2 
        print(f"Inner function: {count}") # Accesses local count (2)
        
    inner_function()
    print(f"Outer function: {count}") # Accesses local count (20)
    
print(f"Global scope: {count}") # Accesses global count (10)
outer_function()
