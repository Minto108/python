numbers = [1,2,3,4]
target = 3
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if(numbers[i] + numbers[j] == target):
            print([i+1,j+1])
        