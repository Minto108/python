class Dog:
    species = "canine"

    def __init__(self,name,age):
        self.name = name
        self.age = age

dog1 = Dog("Harry",4)
print(dog1)
print(dog1.name)