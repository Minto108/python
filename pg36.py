def bracket_pattern(input_str):
    if input_str[0] == ')' or input_str[-1] == '(':
        return False
    pattern = {}
    for i in range(len(input_str)):
        pattern[input_str[i]] = 1 + pattern.get(input_str[i], 0)
    
    if pattern['('] != pattern.get(')', 0):
        return False
    return True
    
    
input_str="()((()()))"
print(bracket_pattern(input_str))