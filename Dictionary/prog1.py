# program to count the frequencyof words in a string
str=input("enter the string:")
l={}
for i in str:
    if(i not in l.keys()):
        l[i]=1
    else:
        l[i]+=1
print(l)