ans = []
while True:
    try:
        a,b = map(int,input().split())
        ans.append((a^b))
    except:
        break
for i in ans:
    print(i)

