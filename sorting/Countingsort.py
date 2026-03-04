'''
Counts how many times each element appears and uses that to determine their sorted positions.
Works only for integers within a small known range.
look up on all elements in the array and keep on incrementing
thr respective position in the answer list'''
#large integers !!
# O(k+N) k->max of array

T = [2,1,3,4,5,2,4,2,6,7,5,8,9,1]
def counting_sort(arr):
    maxx=max(arr)
    counts=[0]*(maxx+1)

    for i in arr:
        counts[i]+=1
    num=0
    for j in range(maxx+1):
        while counts[j]>0:
            arr[num]=j
            num+=1
            counts[j]-=1
counting_sort(T)
print(T)