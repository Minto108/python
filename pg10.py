def calculate(distance, no_of_passengers):
    profit = no_of_passengers * 80 - (distance / 10) * 70
    return int(profit) if profit > 0 else -1


distance = 20
no_of_passengers = 50
print(calculate(distance,no_of_passengers))