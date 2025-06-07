# n --> number of elements, p --> number of cells
# Variations = n ^ p --> with repetition
# Variations = n! / (n-p)! --> with out repetition

def Variations_with_repetition(n,p):
    return n ** p

def factorial(num):
    if num < 0: return "Factorial is not defined for negative numbers"
    
    if num == 0 or num == 1: return 1
    
    return num * factorial(num - 1)

def Variations_without_repetition(n,p):
    if p > n: return 'p must >= n'
    
    return factorial(n) // factorial(n - p)

print(Variations_without_repetition(5, 2))