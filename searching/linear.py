''' 
1. You check each element one by one until you find the target or reach the end.
2. both sorted and unsorted
simple brute force check all
O(n) time and O(1) space'''
sample = [1,3,4,8,7,2]
target = 3
for i in range(len(sample)-1):
    if target == sample[i]:
        print(i+1)
        break
else:
    print("not found")