size=7
m=size-1
for i in range(size):
    for j in range(m,0,-1):
        if j>=i:
            print(end="  ")
    for j in range(0,i):
        if j<=i:
            print("*", end=" ")
    print("\r")
n=size
