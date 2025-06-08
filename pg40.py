def list123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1,2,3]:
            return True
    return False

    

nums=[1,1,2,4,3,4,5]
print(list123(nums))