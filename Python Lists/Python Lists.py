if __name__ == '__main__':
    N = int(input())
    ansList = []  

    for _ in range(N):
        inputed = input().split()  
        rec = inputed[0]  

        if rec == 'insert':
            i = int(inputed[1])  
            e = int(inputed[2])  
            ansList.insert(i, e)
        elif rec == 'print':
            print(ansList)
        elif rec == 'remove':
            e = int(inputed[1]) 
            ansList.remove(e)
        elif rec == 'append':
            e = int(inputed[1]) 
            ansList.append(e)
        elif rec == 'sort':
            ansList.sort()
        elif rec == 'pop':
            ansList.pop()
        elif rec == 'reverse':
            ansList.reverse()

