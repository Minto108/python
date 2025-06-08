def create_new_dictionary(prices):
    new_dict = {}
    for element in prices:
        if prices[element] > 200:
            new_dict[element] = prices[element]
    
    return new_dict

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 200.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))