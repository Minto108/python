def human_pyramid(no_of_people):
    return 1 * 50 if no_of_people == 1 else 50 + human_pyramid(no_of_people - 2)

def find_maximum_people(max_weight):
    max_people = max_weight / 50
    max_people -= 1 if max_people % 2 == 0 else 0
    return max_people if max_weight >= human_pyramid(max_people) else 0

print(find_maximum_people(1000))
 