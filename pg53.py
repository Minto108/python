class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1 = Mobile("Apple", 20000)
mob2 = mob1

mob2.price = 30000

print(mob1.price)

                                                    