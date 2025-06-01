def find_pairs_of_numbers(num_list,n):
    count = 0
    unique = set()
    for element in num_list:
        if element not in unique and element > 0:
            unique.add(element)
        else:
            print("Duplicate value found")
            break

    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == n:
                count += 1
    return count


    

print(find_pairs_of_numbers([2,3],4))


