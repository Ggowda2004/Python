array=[2,4,5,6,7,8,3,10]
def bin_search(nums,target):
    nums.sort()
    while len(nums)!=0:
        mid=len(nums)//2
        if target==nums[mid]:
            return ("found")
        elif target<nums[mid]:
            nums=nums[:mid]
        else:
            nums=nums[mid+1:]
    return False

print(bin_search(array,8))