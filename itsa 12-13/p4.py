n = int(input())
ans = 0
rate = 1.36
spent_rate = 1.02
for i in range(1,n+1):
    ans=((50000*(rate**i))-(10000*(spent_rate**i)))//(35.2-0.2*i)
print(int(ans))
