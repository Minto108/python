my_list = [45,12,78,89,21,4,0,1]
minValue = []
for i in range(0,len(my_list)):
    for j in range(0,len(my_list)-1):
        if my_list[j] > my_list[j+1]:
            temp = my_list[j+1]
            my_list[j+1] = my_list[j]
            my_list[j] = temp
print(my_list)

