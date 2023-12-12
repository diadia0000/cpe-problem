import sys
n = int(input())
space = input()
for j in range(n):
    Trees = {}
    count = 0
    while True:
        tree = sys.stdin.readline().strip("\n")
        if tree == "":
            break
        if tree not in Trees:
            Trees[tree] = 1
        else:
            Trees[tree]+=1
        count+=1
    Trees = dict(sorted(Trees.items()))
    #print(Trees)
    for i in Trees:
        sys.stdout.write(f"{i} {(Trees[i]/count)*100:.4f}\n")
    if j<n-1:
        print()
