class Dog:
    species = "canine"
    
    def __init__(self,name,age):
        self._name = name
        self.__age = age
    def sound(self):
        print("wooooof!!")
    def get_age(self):
        return self.__age

class Labrador(Dog):
    def sound(self):
        print("Woof")

dog1 = Dog("Harry",4)

print(dog1._name)
print(dog1.get_age())
dog2 = Labrador("Ham",5)
print(dog2._name)
print(dog1._name)
dog1.sound()
dog2.sound()