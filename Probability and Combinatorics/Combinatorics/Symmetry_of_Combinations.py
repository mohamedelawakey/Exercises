#c (n,p) == c(n, n-p)

def factorial(num):
    if num < 0: return "Factorial is not defined for negative numbers"
    if num == 0 or num == 1: return 1
    return num * factorial(num - 1)
    
def Symmetry_of_Combinations(n,p):
    return factorial(n) // factorial(p) * factorial(n - p)

n, r = 7, 3
print(f"C({n},{r}) = {Symmetry_of_Combinations(n, r)}")
print(f"C({n},{n - r}) = {Symmetry_of_Combinations(n, n - r)}")