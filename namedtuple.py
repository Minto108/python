from collections import namedtuple

point = namedtuple('point','x y z')
newpoint = point(2,4,5)
print(list(filter(lambda x : x % 2 == 0, newpoint)))

point = namedtuple('point', ['x','y','z'])
newpoint = point(5,6,8)
print((newpoint._asdict()))