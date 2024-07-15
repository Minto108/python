n,m = map(int, input().split())
list1 = list(map(int, input().split()))

for i in range(n):
    count = 0
    for j in range(n):
        if i != j and i + j == m:
            count = 1
            break
if count > 0:
        print("Yes")
else:
        print("No")

