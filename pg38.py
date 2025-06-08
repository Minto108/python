def find_nine(nums):
    if len(nums) < 4:
        return True if 9 in nums else False
    else:
        return True if 9 in nums[:4] else False
        

nums=[1,2,9,3,4]
print(find_nine(nums))