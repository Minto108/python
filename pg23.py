def find_duplicates(list_of_numbers):
    duplicate = []
    unique = set()
    for i in list_of_numbers:
        if i in unique and i not in duplicate:
            duplicate.append(i)
        unique.add(i)
    return duplicate

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)