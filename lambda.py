
a = [1,2,3,4,5,6]

newList = list(map(lambda x: x+5,a))
print(newList)

even = list(map( lambda x : x%2 == 0,a))
print(even)

even = list(filter(lambda x : x% 2 == 0,a))
print(even)