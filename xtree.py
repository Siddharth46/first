for i in range(9):
    for j in range(7):
        if j==3 or (i==1 and j in range(2,5)):
            print("*",end="")
        elif (i==3 and j in range(1,6)) or (i==6 and j in range(0,7)):
            print("*",end="")
        else:
            print(end=" ")
    print()
