''' Divide the array into halves, sort each half recursively, and merge them
Divide array into two halves until single elements remain.
Merge halves in sorted order using a helper function.'''
# time O(n log n)
# space O(n)

N=[2,1,4,3,-1,5,7,33,44,22,66,11]

def merge_sort(arr):
    n=len(arr)
    if n==1:
        return arr
    
    m=len(arr)//2
    L=arr[:m]
    R=arr[m:]

    L = merge_sort(L)
    R=merge_sort(R)
    l,r=0,0
    L_len = len(L)
    R_len=len(R)

    sorted_arr=[0]*n
    i=0
    while l<L_len and r<R_len:
        if L[l]<R[r]:
            sorted_arr[i]=L[l]
            l+=1
        else:
            sorted_arr[i]=R[r]
            r+=1
        i+=1
    while l<L_len:
        sorted_arr[i]=L[l]
        l+=1
        i+=1
    while r<R_len:
        sorted_arr[i]=R[r]
        r+=1
        i+=1
    return sorted_arr
print(merge_sort(N))

#tricky but most used