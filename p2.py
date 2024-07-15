n1 = int(input())
list1 = [int(input()) for _ in range(n1)]

n2 = int(input())
list2 = [int(input()) for _ in range(n2)]

if n1 == n2 and sum(list1) == sum(list2):
    print("Same")
else:
    print("Not Same")