def deg(n):
    if n==9:
        return 1
    else:
        num = list(map(int,str(n)))
        n = sum(num)
        return 1+deg(n)

while True:
    n = int(input())
    if n == 9:
        print(f"{n} is a multiple of 9 and has 9-degree {1}.")
    #print(n)
    if n == 0:
        break
    if n%9!=0:
        print(f"{n} is not a multiple of 9.")
    else:
        degree = deg(n)
        print(f"{n} is a multiple of 9 and has 9-degree {degree-1}.")