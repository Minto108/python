def find_smallest_number(num):
    if num <= 0:
        raise ValueError("Enter a positive integer")
    
    def divisor_number(current_number):
        count = 0
        for i in range(1, current_number + 1):
            if current_number % i == 0:
                count += 1
        return count
    
    current_number = 1

    while True:
        divisors = divisor_number(current_number)
        if divisors == num:
            return current_number
        current_number += 1
try:
    num=16
    print("The number of divisors :",num)
    result=find_smallest_number(num)
    print("The smallest number having",num," divisors:",result)
except TypeError:
    print("Invalid data type")
