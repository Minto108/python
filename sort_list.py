
def list_sort(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        else:
            hashset.add(i)
    return False


nums = [1,2,3]
list_sort(nums)