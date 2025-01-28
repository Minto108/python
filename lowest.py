my_list = [7,12,9,7,8]
minVal = my_list[0]
for i in my_list:
    if i < minVal:
        minVal = i
print(minVal)
print(my_list.index(7,2,4)) # finds the index of 7 that is between the indices 2 and 4