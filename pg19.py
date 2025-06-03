def is_palindrome(word):
    return word.lower() == word[::-1].lower()
    


result = is_palindrome("MadAM")

if (result):
    print("Palindrome")
else:
    print("Not a palindrome")
