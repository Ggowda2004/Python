'''
divide the array in half each time — compare the middle element,
then decide whether to go left or right.
use mid <> then move as you need
time O(logn) and spaceO(1)
works only for sorted array'''
s=[1,2,3,4,5,7,8,9,10]
start=0
end=len(s)-1
target= 6
while start<=end:
    mid=(start+end)//2
    if s[mid]==target :
        print("num found", mid+1)
        break
    elif s[mid]>target:
        end=mid-1
    else:
        start = mid+1
else:
    print("no number")

