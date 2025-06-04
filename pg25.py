def check_anagram(data1,data2):
    if len(data1) != len(data2):
        return False
    data1 = data1.lower()
    data2 = data2.lower()
    for i in range(len(data1)):
        if data1[i] == data2[i]:
            return False

    countS = {}
    countT = {}

    for i in range(len(data1)):
        countS[data1[i]] = 1 + countS.get(data1[i],0)
        countT[data2[i]] = 1 + countT.get(data2[i],0)
    
    for i in countS:
        if countS[i] != countT.get(i,0):
            return False
    return True



print(check_anagram("About","table"))
