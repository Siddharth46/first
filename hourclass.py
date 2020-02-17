size=7
m=size-2
for i in range(size,-1,-1):
    for j in range(m,0,-1):
        print(end=" ")
    m=m+1
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")
m=(2*size)-2
for i in range(0,size+1):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")
