import sys
def switch(a,b):
    return b,a
while True:
    a,b = sys.stdin.readline().strip("\n").split()
    if a == "0" and b == "0":
        break
    if len(b)>len(a):
        a,b = switch(a,b)
    a = a[::-1]
    b = b[::-1]
    num = []
    c = 0
    for i in range(0,len(a)):
        if c >len(b)-1:
            num.append(int(a[i]))
        else:
            num.append(int(a[i])+int(b[i]))
        c+=1
    #print(num)
    carry = 0
    for j in range(len(num)):
        if num[j]>=10 and j!=len(num)-1:
            carry+=1
            num[j+1]+=1
        elif num[j]>=10 and j == len(num)-1:
            carry+=1
    if carry == 0:
        print("No carry operation.")
    else:
        if carry == 1:
            print(f"{carry} carry operation.")
        else:
            print(f"{carry} carry operations.")
