n = 5
k = 0
for i in range(1,n+1) : #row 6 

    # Print spaces 
    for j in range(i,n) : 
            print(' ', end='') 
    # Print # 
    while (k != (2 * i - 1)) : 
        if (k == 0 or k == 2 * i - 2) : 
            print('#', end='') 
        else : 
            print(' ', end ='') 
        k = k + 1
    k = 0; 
    print ("") # print next row 
          
    # print last row 
