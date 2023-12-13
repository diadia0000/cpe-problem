n = int(input())
Map = [0 for i in range(25)]
kitchen = [int(i) for i in input().split()]
for i in range(0,len(kitchen),2):
    for j in range(kitchen[i]+1,kitchen[i+1]+1):
        Map[j]+=1
print(max(Map))
