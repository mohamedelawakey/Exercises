def BinarySearch(the_lest, target, left, right):
    if left > right:
        return -1
    
    middle = (left + right) // 2
    
    if the_lest[middle] == target:
        return middle
    elif the_lest[middle] < target:
        return BinarySearch(the_lest, target, middle + 1, right)
    else:
        return BinarySearch(the_lest, target, left, middle - 1)

# try

my_list = [5, 10, 15, 20, 25, 30, 35]
target1, target2 = 4, 25

result1 = BinarySearch(my_list, target1, 0, len(my_list) - 1)
result2 = BinarySearch(my_list, target2, 0, len(my_list) - 1)

if result1 != -1:
    print(f"Element found at index: {result1}")
else:
    print("Element not found")
    
if result2 != -1:
    print(f"Element found at index: {result2}")
else:
    print("Element not found")