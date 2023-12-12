while True:
    try:
        num = list(map(int,input().split()))[1:]
        if len(num) == 1:
            print("Jolly")
            continue
        check = False
        n = len(num)-1
        ans = [0]*(n+1)
        for i in range(0,len(num)):
            l,r = 0,0
            if (i-1)<0:
                r = abs(num[i]-num[i+1])
            elif (i+1)>len(num)-1:
                l = abs(num[i]-num[i-1])
            else:
                r = abs(num[i]-num[i+1])
                l = abs(num[i]-num[i-1])
            if (r>n) or (l>n):
                check = True
                break
            ans[r] = 1 ; ans[l] = 1
        if check:
            print("Not jolly")
        else:
            for j in range(1,len(ans)):
                if ans[j] == 0:
                    print("Not jolly")
                    check = True
                    break
            if not check:
                print("Jolly")
    except:
        break
