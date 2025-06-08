def count_digits_letters(sentence):
    return [sum(1 for letter in sentence if letter.isalpha()),
            sum(1 for letter in sentence if letter.isdigit())]

sentence="Infosys 123"
print(count_digits_letters(sentence))