class Vehicle:
    def __init__(self, mileage, fuel_left):
        self.mileage = mileage
        self.fuel_left = fuel_left
        self.reserve_fuel = 5

    def identify_distance_that_can_be_travelled(self):
        usable_fuel = self.fuel_left - self.reserve_fuel
        return 0 if self.fuel_left <= self.reserve_fuel else (self.mileage * (usable_fuel))
    
    def identify_distance_travelled(self, initial_fuel):
        used_fuel = initial_fuel - self.fuel_left
        return self.mileage * (used_fuel) if initial_fuel > self.fuel_left else None
    

car1 = Vehicle(15,10)
print(car1.identify_distance_that_can_be_travelled())
print(car1.identify_distance_travelled(30))

print(car1)