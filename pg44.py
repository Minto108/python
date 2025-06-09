def calculate_net_amount(trans_list):
    net_amount = 0
    for i in trans_list:
        action, amount = i.split(":")
        net_amount = net_amount + int(amount) if action == 'D' else net_amount - int(amount)
    
    return net_amount

trans_list=["D:350","W:100","W:500","D:1000"]
print(calculate_net_amount(trans_list))