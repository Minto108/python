def seed_no(number,ref_no):
    total = number
    
    for i in str(number):
        total *= int(i)
    return total == ref_no
# from math import prod
# def seed_no(number, ref_no):(
#   product = prod(int(i) for i in str(number)))
#   return number * product == ref_no
number = 123
ref_no = 738
print(seed_no(number,ref_no))