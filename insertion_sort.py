my_list = [12,45,6,8,9]
for i in range(1,len(my_list)):
    start_index = i
    current_value = my_list[i]
    for j in range(i-1,-1,-1):
        if current_value > my_list[j]:
            break
        else:
            my_list[j+1] = my_list[j]
            start_index = j
    my_list[start_index] = current_value
print(my_list)