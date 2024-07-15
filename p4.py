n1 = int(input())
list1 = [int(input()) for _ in range(n1)]

n2 = int(input())
list2 = [int(input()) for _ in range(n2)] 

if n1 == n2:
    for i in range(n1):
        count = 0
        if list1[i] < list2[i]:
            count += 1
    if count == 0:
        print("Compatible")
    else:
        print("Incompatible")
else:
    print("Incompatible")