def nearest_palindrome(number):
    
    while True:
        num = str(number)
        if num == num[::-1]:
            return int(num)
        number += 1

number = 12421
print(nearest_palindrome(number))
        
