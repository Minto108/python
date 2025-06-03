def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    primes = []
    for number in list_of_factors:
        result = is_prime(number, number // 2)
        if result:
            primes.append(number)
    return max(primes)

def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    factors = find_factors(num)
    return find_largest_prime_factor(factors)

def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    sums = 0
    for i in range(num,num+9):
        sums += find_f(i)
    return sums

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))