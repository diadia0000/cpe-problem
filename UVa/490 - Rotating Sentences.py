word = []
max_len = 0
while True:
    try:
        n = input()
        max_len = max(len(n),max_len)
        word.append(n)
    except:
        break
#print(word)
print(max_len)
for i in range(max_len):
    for j in range(len(word)-1,-1,-1):
        if i > len(word[j])-1:
            print(' ',end='')
        else:
            print(word[j][i],end='')
    print()

    