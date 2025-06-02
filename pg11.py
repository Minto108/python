list_of_marks = (12,18,25,24,2,5,18,20,20,21)


def find_more_than_average():
    count = 0
    average = sum(list_of_marks) / len(list_of_marks)
    for mark in list_of_marks:
        if  mark > average:
            count += 1
    return (count / len(list_of_marks)) * 100

def generate_frequency():
    freq = [0] * (max(list_of_marks) + 1)
    for mark in list_of_marks:
        freq[mark] += 1
    return freq

def sort_marks():
    return sorted(list_of_marks)



print(find_more_than_average())
print(generate_frequency())
print(sort_marks())