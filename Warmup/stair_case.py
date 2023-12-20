def staircase():
    arr_value = 6

    for i in range(arr_value):
        for j in range(i,arr_value-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
staircase()