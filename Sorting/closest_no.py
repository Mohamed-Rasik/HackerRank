def closest():

    arr_size = 12
    arr_values = [-20, -3916237, -357920, -3620601 ,7374819 ,-7330761, 30, 6246457, -6461594, 266854, -520 ,-470]

    arr_values.sort()

    minimum_difference = float("inf")
    for i in range(1,len(arr_values)):
        difference = arr_values[i] - arr_values[i - 1]
        minimum_difference = min(minimum_difference,difference)

    result=[]
    for i in range(1,len(arr_values)):
        difference = arr_values[i] - arr_values[i-1]
        if minimum_difference == difference:
            result.extend([arr_values[i-1],arr_values[i]])
    return result 
    
final=closest()
print(*final)