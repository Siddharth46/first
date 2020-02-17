h=7
m=(2*h)-2
for i in range(0,h-1):
    for j in range(0,m):
        print(end=" ")
    m=m-2
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")
m=-1
for i in range(h-1,-1,-1):
    for j in range(m,-1,-1):
        print(end=" ")
    m=m+2
    for j in range(0,i+1):
        print("*", end=" ")
    print("\r")
