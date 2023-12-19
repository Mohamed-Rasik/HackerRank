def sorting():
    
    arr_size = int(input())
    
    arr_values = list(map(int,input().split()))
    
    for i in range (0,arr_size):
        for j in range(i+1,arr_size):
            if arr_values[i] > arr_values[j]:
                arr_values[i],arr_values[j] = arr_values[j],arr_values[i]
        print(" ".join(map(str, arr_values)))

sorting()


