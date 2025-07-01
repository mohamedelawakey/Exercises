def quick_sort(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    
    return arr
    
def partition(arr, low, high):
    pivot = arr[high]
    i = low
    
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[i], arr[high],  = arr[high], arr[i]
    return i

arr = [10, 7, 8, 9, 1, 5]
print("Original:", arr)
print("Sorted:", quick_sort(arr.copy())) 