class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

mob1 = Mobile("Apple", 20000)
print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)

mob2 = Mobile("Samsung", 30000)
print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)