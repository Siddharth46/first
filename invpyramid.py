size=8
halfw=(2*size)-2
for i in range(size,-1,-1):
    for j in range(halfw):
        print(end=" ")
    halfw=halfw+1
    for j in range(0,i+1):
        print("*", end=' ')
    print("\r")
