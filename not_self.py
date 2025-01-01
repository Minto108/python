nums = [1,2,3,4]
product = []
for i in range(len(nums)):
    prod = 1
    for j in range(len(nums)):
        if i == j:
            continue
        prod *= nums[j]
    product.append(prod)
print(product)