import sys
c = 0
while True:
    try:
        n = list(input())
        if c:
            print()
        dit = {}
        for i in n:
            if i not in dit:
                dit[i] = 1
            else:
                dit[i]+=1
        dit = dict(sorted(dit.items(),key = lambda x:(x[1],-ord(x[0]))))
        line = 0
        for j in dit:
            if line == len(dit)-1:
                print(f"{ord(j)} {dit[j]}")
            else:
                sys.stdout.write(f"{ord(j)} {dit[j]}\n")
            line+=1
        c = 1
    except EOFError:
        break
