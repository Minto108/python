def check_well_formatted(input_item,list_label):
    if not isinstance(input_item,list):
        return False
    if len(input_item) < 2:
        return False
    if input_item[0] not in list_label:
        return False
    
    for sub in input_item[1:]:
        if  isinstance(sub, list):
            if not check_well_formatted(sub, list_label):
                return False
        elif not isinstance(sub, str):
            return False
    return True
        

input_list1=['VP', ['V']]
list_label1=['VP', 'V']
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")