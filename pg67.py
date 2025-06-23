def exchange_list(number_list):
    #for i in range(len(number_list)//2):
    #    number_list[i], number_list[len(number_list)-i-1] = number_list[len(number_list)-i-1], number_list[i]
    #return number_list

    return number_list[::-1]



number_list = [1,2,3,4,5,6,7,8,9]
print(exchange_list(number_list))