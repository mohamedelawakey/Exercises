# single
def intersection(a,b):
    return list(set(a) & set(b))

# multiable
def intersection_multiple(*lists):
    if not lists:
        return []
    
    result = set(lists[0])
    for lst in lists[1:]:
        result &= set(lst) 
    return list(result)


x = [1, 2, 3, 4]
y = [2, 3, 5]
z = [0, 2, 3, 9]
print(intersection_multiple(x,y,z))

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

print(intersection(A, B)) 