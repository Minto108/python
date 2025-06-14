class Customer:

    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    
    def update_balance(self, amount):
        if 0 < amount < 1000:
            self.__wallet_balance += amount
    
    def show_balance(self):
        print("The balance is", self.__wallet_balance)


c1 = Customer(1001, "Don", 23, 10000)
c1.update_balance(500)
c1.show_balance()