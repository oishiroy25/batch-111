def duplicate(nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k=k+1
    return k



nums=[2,2,3,3,4,4,5]
x=duplicate(nums)
print(x)
print(nums[:x])