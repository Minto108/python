class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price
    
    def purchase(self):
        print("Purchasing a mobile")
        print("The mobile has brand", self.brand, "and price", self.price)


mob1 = Mobile("Apple", 20000)
mob1.purchase()

mob2 = Mobile("Samsung", 15000)
mob2.purchase()