def factorial(number):
    return 1 if number == 1 or number == 0 else number * factorial(number - 1)

def find_strong_numbers(num_list):
    strong = []
    for num in num_list:
        num = str(num)
        total = 0
        total = sum(factorial(int(num[i])) for i in range(len(num)))

        if total == int(num):
            strong.append(int(num))
    return strong

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)