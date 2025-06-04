def remove_duplicates(value):
    unique = set()
    result = []
    for i in value:
        if i not in unique:
            unique.add(i)
            result.append(i)
    return ''.join(result)
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))