def check_double(number):
    num = str(number)
    double = str(number * 2)
    position_elements = {}
    position_double = {}
    if len(num) != len(double):
        return False

    for i in range(len(num)):
        if num[i] in position_elements:
            position_elements[num[i]] += 1
        else:
            position_elements[num[i]] = 1

        if double[i] in position_double:
            position_double[double[i]] += 1
        else:
            position_double[double[i]] = 1
    
    
    for element in (double):
        if element not in position_elements or str(number) == str(double):
            return False
        if position_double[element] != position_elements[element]:
            return False
    return True

            
        
print(check_double(125874))
