N,M = map(int,input().split())
ans = []
rate = [float(i) for i in input().split()]
for i in range(M):
    test = [float(i) for i in input().split()]
    grade = 0
    c = 0
    for i in test:
        grade+=i*rate[c]
        c+=1
    ans.append(grade)
for i in range(len(ans)):
    if i == len(ans)-1:
        print(f"{ans[i]:.2f}")
    else:
        print(f"{ans[i]:.2f}",end = " ")
print(f"{(sum(ans)/M):.2f}")