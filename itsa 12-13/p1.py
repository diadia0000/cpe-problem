n = int(input())
for i in range(n):
    S,K,M,D = map(int,input().split())
    spent = S
    if D>M:
        spent+=(D-M)*(K+5)+(D-(D-M))*K
    else:
        spent+=(D)*K
    print(spent)