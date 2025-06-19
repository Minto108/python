def check_occurence(string):
    
    from collections import Counter
    string_words = Counter(string.lower().split())
    return string_words['jet'] == string_words['mat']
        
string="mat jet Jet Mat"
print(check_occurence(string))