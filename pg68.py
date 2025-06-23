def sum_of_elements(num_list, number):
    total = 0
    for i in range(len(num_list)):
        if i == 0:
            if num_list[1] != number and num_list[i] != number:
                total += num_list[i]
        
        elif i == len(num_list)-1:
            if num_list[i] != number and num_list[i-1] != number:
                total += num_list[i]
        
        elif num_list[i] != number and num_list[i+1] != number and num_list[i-1] != number:
            total += num_list[i]
    return total

num_list = [1,7,3,4,1,7,10,5]
number = 7
print(sum_of_elements(num_list, number))
