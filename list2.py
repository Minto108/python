l=[5,46,87,2,5,4,100]
m=[]
for i in range(0,3):
    m.append(max(l))
    l.remove(max(l))
print(min(m))
