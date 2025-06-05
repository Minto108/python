def check_prime(number):
    if number < 2 :
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
    
        

def rotations(num):
    if check_prime(num) :
        n = str(num)
        return [int(n[i:] + n[:i]) for i in range(len(n))] 


def get_circular_prime_count(limit):
    count = 0
    
    for i in range(2,limit):
        rot_list = rotations(i)
        if rot_list and all(check_prime(r) for r in rot_list):
            count += 1
    return count

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
