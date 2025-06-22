def BinarySearch(the_lest, target):
    left = 0
    right = len(the_lest) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if the_lest[middle] == target:
            return middle
        elif the_lest[middle] > target:
            right = middle - 1
        else: 
            left = middle + 1
            
    return -1

# try
my_list = [5, 10, 15, 20, 25, 30, 35]
target1 = 4
target2 = 25
result1 = BinarySearch(my_list, target1)
result2 = BinarySearch(my_list, target2)

if result1 != -1:
    print(f"Element found at index: {result1}")
else:
    print("Element not found")
    
if result2 != -1:
    print(f"Element found at index: {result2}")
else:
    print("Element not found")