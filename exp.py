for i in range(5):
    for j in range(9):
        if (i==0 and j==4) or (i==3 and j in range(1,8)):
            print("*",end="")
        elif (i==1 and j==3) or (i==2 and j==2) or (i==4 and j==0):
            print("*",end="")
        elif (i==1 and j==5) or (i==2 and j==6) or (i==4 and j==8):
            print("*",end="")
        else:
            print(end=" ")
    print()
