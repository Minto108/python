my_list = [45,12,78,89,21,4,0,1]
for i in range(len(my_list)-1):
    min_index = i
    for j in range(i+1,len(my_list)):
        if my_list[j] < my_list[min_index]:
            min_index = j
    my_list[i],my_list[min_index] = my_list[min_index],my_list[i]
print(my_list)