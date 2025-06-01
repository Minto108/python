def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def find_strong_numbers(num_list):
    strong_nums = []
    for num in num_list:
        sum_fact = 0
        for nums in str(num):
            sum_fact += factorial(int(nums))
        if sum_fact == num:
            strong_nums.append(sum_fact)
    return strong_nums

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)