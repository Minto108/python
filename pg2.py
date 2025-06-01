def func(arg1, arg2, *arg3):
    print(arg1, arg2, arg3)
    for i in arg3:
        print(i)


func(1,2,3,5,9,5,78)