def check_perfect_number(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    return number if total == number else None

def check_perfectno_from_list(no_list):
    return [number for number in no_list if check_perfect_number(number)]

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)