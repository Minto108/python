a=int(input("enter the length of the list:"))
l=[]
m=[]
for i in range(0,a):
    b=int(input("enter the numbers:"))
    l.append(b)

c=int(input("enter the number:"))
for i in l:
    if(i<c):
        m.append(i)
print(m)
