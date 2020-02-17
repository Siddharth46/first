for i in range(6):
    for j in range(11):
        if (i==3 and j in range(0,8)) or (j==7 and (i>0 and i<6)):
            print("*",end="")
        elif ((i>0 and i<4) and j==i-1) or ((i==4 and j==1) or (i==5 and j==0)):
            print("*",end="")
        elif ((i==2 or i==4) and j==9) or (i==3 and j==10):
            print("*",end="")
        else:
            print(end=" ")
    print()
