def union_of_two_events(a,b):
    return list(set(a) | set(b))

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

print(union_of_two_events(A, B)) 