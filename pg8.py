def odd(data):
    return [num for num in data if num % 2 != 0]

def even(data):
    return [num for num in data if num % 2 == 0]

def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func == None:
        return sum(list_of_num)
        #sum_elements = 0
        #for element in list_of_num:
            #sum_elements += element
        #return sum_elements
    return sum(filter_func(list_of_num))


sample_data = range(1,11)
print(sum_of_numbers(sample_data,even))

