n=4
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()
n=n-1
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j>=i:
            print("* ",end="")
    print()
