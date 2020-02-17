for i in range(7):
    for j in range(9):
        if ((i==0 or i==6) and j!=4) or j==0 or j==8:
            print("*",end="")
        elif (i==1 or i==5) and (j<3 or j>5):
            print("*",end="")
        elif (i==2 or i==4) and (j<2 or j>6):
            print("*",end="")
        else:
            print(end=" ")
    print()
