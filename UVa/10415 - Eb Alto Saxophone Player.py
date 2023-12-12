def is_type(a,b):
    for m in range(a,b):
        if is_push[m] == 0:
            finger[m]+=1
            is_push[m] = 1
t = int(input())
for i in range(t):
    finger = [0 for f in range(11)]
    play = [_ for _ in input()]
    is_push = [0 for f in range(11)]
    if play == [""]:
        print(*finger[1:])
        continue
    for x in play:
        if x == "c":
            is_type(2,5) ; is_type(7,11)
            is_push[1] = 0 ;is_push[5] = 0;is_push[6] = 0
        elif x == "d":
            is_type(2,5) ; is_type(7,10)
            is_push[1] = 0 ; is_push[5] = 0 ;is_push[6] = 0 ; is_push[10]=0
        elif x == "e":
            is_type(2,5) ; is_type(7,9)
            is_push[1] = 0 ; is_push[5] = 0 ;is_push[6]=0 ; is_push[9]=0 ; is_push[10]=0
        elif x == "f":
            is_type(2,5)
            if is_push[7] == 0:
                finger[7] += 1
                is_push[7] = 1
            is_push[1] = 0 ; is_push[5:7] = (0,0)
            is_push[8:11] = (0,0,0)
        elif x == "g":
            is_type(2,5)
            is_push[1] = 0 ; is_push[5:11] = (0,0,0,0,0,0)
        elif x == "a":
            is_type(2,4)
            is_push[1] = 0 ; is_push[4:11] = (0,0,0,0,0,0,0)
        elif x == "b":
            is_type(2,3)
            is_push[1] = 0 ; is_push[3:11] = (0,0,0,0,0,0,0,0)
        elif x == "C":
            is_type(3,4)
            is_push[1:3] = (0,0) ; is_push[4:11] = (0,0,0,0,0,0,0)
        elif x == "D":
            is_type(1,5) ; is_type(7,10)
        elif x == "E":
            is_type(1,5) ; is_type(7,9)    
        elif x == "F":
            is_type(1,5)
            if is_push[7] == 0:
                finger[7] += 1
                is_push[7] = 1
        elif x == "G":
            is_type(1,5)
        elif x == "A":
            is_type(1,4)
        elif x == "B":
            is_type(1,3)
    print(finger)



