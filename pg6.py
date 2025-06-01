#PF-Tryout
#Start writing your code here
def find_grade(score):
    if 80 <= score <= 100:
        print("A")
    elif 73 <= score <= 79:
        print("B")
    elif 65 <= score <= 72:
        print("C")
    elif 0 <= score <= 64:
        print("D")
    else:
        print("Z")

score = 80
find_grade(score)