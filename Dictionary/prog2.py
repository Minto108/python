x={'k1':'v1','k2':'v2','k3':'v3'}
print(x)
l=[]
y={}
d=0
for i in x.keys():
    l.append(i)
l=len(l)
m=0
for i in x.values():
    a=l[d]
    y[i]=tuple(a)
    d=d+1

print(y)









    