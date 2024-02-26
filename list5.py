a=int(input("enter the length of the list1:"))
b=int(input("enter the length of the list2:"))
l=[]
m=[]
common=[]
print("enter the elements of list1")
for i in range(0,a):
    c=int(input("enter the elements of the list1:"))
    l.append(c)

print("enter the elements of list2")
for i in range(0,b):
    d=int(input("enter the elements of the list2:"))
    m.append(d)

for i in l:
    for j in m:
        if(i==j):
            if(i not in common):
                common.append(i)

print(common)