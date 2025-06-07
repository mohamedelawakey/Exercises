# Permutations is a factorial

def Permutations(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    
    if num == 0 or num == 1:
        return 1
    
    return num * Permutations(num - 1)
    
print(Permutations(5))