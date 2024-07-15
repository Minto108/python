n = int(input())
# the inputs are space separated
list1 = list(map(int, input().split()))

odd = []
even = []

for i in range(n):
    if list1[i] % 2 == 0:
        even.append(list1[i])
    else:
        odd.append(list1[i])
list1.clear()
list1 = even  + odd
print(list1)
