a=int(input("enter the length of the list:"))
l=[]
m=[]
for i in range(0,a):
    b=int(input("enter the element:"))
    l.append(b)

for i in l:
    if(i%2==0):
        m.append(i)
m.sort()

print(m)