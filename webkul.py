n=int(input())
if n==1:
    for i in range(n+1):
        print(" " *(n-i)+"*"*(3*n+6*i))
elif(n==2):
    for i in range(3):
        for j in range(13):
            if(i in {0,1} and j in {3,5}):
                print("*",end="")
            elif(i==2 and j in {1,2,3,4,6,7,8,9,10,11,12}):
                print("*",end="")
            else:
                print(" ",end="")
        print()
elif(n==3):
    for i in range(4):
        for j in range(6):
            if(i in {0,1,2} and j==0):
                print("*",end="")
            elif(i==3 and j in {0,1,2,3,4,5}):
                print("*",end="")
            else:
                print(" ",end="")
        print()
else:
    print("",end="\n")

