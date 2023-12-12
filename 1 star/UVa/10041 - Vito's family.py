def count(near):
    ans = 0
    for i in range(len(family)):
        ans+=abs(family[i]-family[near])
    return ans
n = int(input())
for i in range(n):
    near = 0
    family = [int(i) for i in input().split()]
    home = family[0] ; del(family[0])
    family.sort()
    near = len(family)//2
    ans = count(near)
    print(ans)