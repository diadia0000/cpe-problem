import sys
while True:
    n = str(sys.stdin.readline().strip("\n")) #speed up
    if int(n) == 0:
        break
    if int(n)%11==0:
        print(f"{n} is a multiple of 11.")
    else:
        print(f"{n} is not a multiple of 11.")