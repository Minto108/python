def find_upper_and_lower(sentence):
    return [sum(1 for i in sentence if i.isupper()),
            sum(1 for i in sentence if i.islower())]

sentence = "Hello world!"
print(find_upper_and_lower(sentence))