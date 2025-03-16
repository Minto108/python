n1 = int(input())
n2 = int(input())

a,b = [],[]

for i in range(n1):
    a.append(int(input()))

for i in range(n2):
    b.append(int(input()))
    
c = list(set(a+b))
c.sort()

l = len(c)

if l % 2 == 0:
    print((c[l//2] + c[l//2 - 1]) / 2)
else:
    print(c[l//2])
