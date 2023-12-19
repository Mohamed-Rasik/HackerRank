def alter_char():
    q=int(input())

    for i in q:
        s=input()

    new = s[0]

    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new += s[i+1]
    return len(s) - len(new)
final=alter_char()
print(final)
