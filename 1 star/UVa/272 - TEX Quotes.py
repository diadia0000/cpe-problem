count = 0
while True:
    try:
        n = input()
        for i in n:
            if i == '"':
                if count%2==0:
                    print("``",end="")
                else:
                    print("''",end="")
                count+=1
            else:
                print(i,end = "")
        print()
    except:
        break