test = int(input())
for i in range(test):
    n = int(input())
    if n<0:
        print((bin(0b11111111111111111111111111111111+n+1)[2:]).count("1"))
    else:
        ans = bin(n)[2:]
        print(("0"*(32-len(ans))+ans).count("1"))


