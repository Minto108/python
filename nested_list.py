if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name,score])
    hashset = sorted(set(score for name, score in record))
    
    mscore = hashset[1]
    
    names = [name for name, score in record if score == mscore]
    names.sort()
    
    for i in names:
        print(i)