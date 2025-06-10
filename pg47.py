def calculate_expenditure(list_of_expenditure):
    total = 0
    try:
        print(sum(list_of_expenditure))
        avg = total / no_values
        print(avg)
    except NameError:
        print("Invalid name")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Please insert integer values")
    except:
        print("Some error occured")
    
    finally:
        print("It's been an exciting journey")





list_of_values = [100,200,300,400,500]
calculate_expenditure(list_of_values)