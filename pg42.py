def even(number):
    if number % 2 == 0:
        return number
    

print(list(map(even, [1,2,3,45,6,7,8])))