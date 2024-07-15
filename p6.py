n = int(input())
odd = 0
even = 0

list1 = [int(input()) for _ in range(n)]
for i in range(n):
    if list1[i] % 2 == 0:
        even = even + list1[i]
    else:
        odd = odd + list1[i]
print(f"The sum of the even numbers in the array is {even}")
print(f"The sum of the odd numbers in the array is {odd}")



