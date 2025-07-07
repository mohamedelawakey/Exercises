def compAndSwap(a, i, j, dire):
    if(dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a, low, count, dire):
    if count > 1:
        k = count // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, low, dire)
        
def bitonicSort(a, low, count, dire):
    if count > 1:
        k = count // 2
        
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, low, 0)
        bitonicMerge(a, low, count, dire)
    
def sort(a, n, up):
    bitonicSort(a, 0, n, up)

arr = [3, 7, 4, 8, 6, 2, 1, 5]
sort(arr, len(arr), 1)  
print(arr)