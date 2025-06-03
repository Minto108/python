def human_tower(no_of_people):
    return 1 * 50 if no_of_people == 1 else no_of_people * 50 + human_tower(no_of_people - 2)
    

print(human_tower(5))