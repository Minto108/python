n,m = map(int, input().split())
list1 = list(map(int, input().split()))
count = 1
temp = m
for i in range(n):
    if list1[i] <= m:
        m = m - list1[i]
    else:
        count = count + 1
        m = temp - list1[i]
print(count)
