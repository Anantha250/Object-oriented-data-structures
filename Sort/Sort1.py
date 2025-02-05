def bubblesortRecursive(list):
    cnp = 0
    for i in range(len(list)):
        for j in range(len(list)-1-i):
           cnt+= 1
           if list[j] < list[j+1]:
               list[j],list[j+1] = list[j+1],list[j]
    
    print(cnp)

inp = list(map(int,input("Enter Input :").split()))
bubblesortRecursive(inp)
print(inp)
    