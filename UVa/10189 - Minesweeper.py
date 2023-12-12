def show(Map):
    for i in range(n):
        for j in range(m):
            print(Map[i][j],end = "")
        print()
field = 1
dirt =[[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
c = 0
while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    
    Map = []
    for x in range(n):
        Map.append(list(input()))
    #show(Map)
    Ans = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if Map[i][j] == "*":
                Ans[i][j] = "*"
            else:
                for k in dirt:
                    if i+k[0]<n and i+k[0]>=0 and j+k[1]<m and j+k[1]>=0:
                        if Map[i+k[0]][j+k[1]] == "*":
                            Ans[i][j] +=1
    if c:
        print()
    print(f"Field #{field}:") 
    show(Ans)
    field+=1
    c+=1
