import sys
while True:
    n = int(input())
    if n == 0:
        break
    Bin = str(bin(n))
    count_one = Bin.count("1")
    print(f"The parity of {Bin[2:]} is {count_one} (mod 2).")
