In = input().split()
card = []
for i in In:
    l,r = i[0],i[1]
    if l == "A" or l == "a":
        l = 14
    elif l == "t" or l == "T":
        l = 10
    elif l == "J" or l == "j":
        l = 11
    elif l == "Q" or l == "q":
        l = 12
    elif l == "K" or l == "k":
        l = 13
    card.append([int(l),r.lower()])
card.sort(key = lambda x:x[0])
flag_color = True
flag_num = True
count = card[0][0]
for i in range(1,5):
    if int(card[i][0]) == count+1:
        count = int(card[i][0])
    else:
        flag_num = False
        break

now = card[0][1]
for i in range(1,5):
    if card[i][1] != now:
        flag_color = False
        break
if flag_num == True and flag_color == True:
    print("ys")
elif flag_color == True and flag_num == False:
    print("s")
elif flag_color == False and flag_num == True:
    print("y")
else:
    print("n")


