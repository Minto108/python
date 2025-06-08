#static method and class method

class person(object):
    population = 50

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def getPopulation(cls):
        return cls.population
    
    @staticmethod
    def isAdult(self):
        return self.age > 18
    
    # since it is a static method it cannot access age from the class
    # so you have to pass the value manually    
    def display(self):
        print(self.name, "is", self.age, "years old")


newPerson = person('minto', 22)
print(newPerson.isAdult(newPerson))
print(newPerson.age)
newPerson.display()
print(person.getPopulation())
