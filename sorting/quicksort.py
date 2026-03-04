'''Pick a pivot element, partition the array into two subarrays 
— smaller and greater — and sort each recursively.
Choose a pivot (usually the last element).
Rearrange (partition) elements:
Elements ≤ pivot on the left.
Elements > pivot on the right.'''
#not stable like merge_sort because seleting 
# right pivot element is luck O(n log n), if we get bad pivotO(n2)

A=[2,1,3,2,4,5,4,6,77,65,32,11,44,55,66,6]
def Quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    L = [x for x in arr[:-1] if x<=pivot]
    R=[x for x in arr[:-1] if x>pivot ]
    
    L= Quick_sort(L)
    R= Quick_sort(R)

    return L+[pivot]+R
print(Quick_sort(A))
