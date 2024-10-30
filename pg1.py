shoes = int(input())
arr = list(map(int,input().split()))
cust = int(input())
money = 0
for i in range(cust):
    size, price = list(map(int,input().split()))
    if size in arr:
        money += price
        arr.remove(size)
print(money)