def even(list_of_num):
        if list_of_num % 2 == 0:
            return list_of_num
        
list1 = [2,3,4,5]
#print(list(filter(None,map(even,list1))))
print(list(filter(even, list1)))