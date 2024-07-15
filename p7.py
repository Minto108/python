n = int(input())
num = [int(input()) for _ in range(n)]
print("The Sorted array is:")
num.sort()
for i in range(n):
    print(num[i])