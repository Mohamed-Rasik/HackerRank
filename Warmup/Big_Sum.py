def bigsum():
    n=int(input())
    arr = list(map(int,input().split()))

    result = 0

    for i in range(n):
        result += arr[i]
    return result
final=bigsum()
print(final)