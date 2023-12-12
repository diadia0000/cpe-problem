import decimal
while True:
    n = int(input())
    if n == 0:
        break
    cost = []
    total = 0.00
    for i in range(n):
        std = float(input())
        cost.append(std)
        total+=std
    total/=float(n)
    ans = 0
    for j in cost:
        if total-j>0:
            ans+=(total-j)
    print(f"${decimal.Decimal(ans):.2f}")
