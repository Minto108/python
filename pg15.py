def find_average(mark_list):
    total = 0
    try:
        for i in range(0, len(mark_list)):
            total+=mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except ZeroDivisionError:
        print("Empty list")
    except IndexError:
        print("Index out of bound")
    except TypeError:
        print("Wrong data type")
    except NameError:
        print("Invalid variable")
    except:
        print("Some other error")
    finally:
        print("Program executed")

try:
    m_list=[1,2,3,4]
    print("Average marks:", find_average(m_list))
except ValueError:
    print("Invalid parameter")