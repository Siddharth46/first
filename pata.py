for i in range(6):
    for j in range(6):
        if i==3 or (i in range(2,6) and (j==0 or j==5)):
            print("*",end="")
        elif ((j==2 or j==3) and i==0) or (i==1 and j==1) or (i==1 and j==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
