n = int(input())
move = list(map(str, input().split()))


x,y = 1,1
mid = []
cnt = 0

#for i in range(n):
#    for j in range(n):
#        mid.append((x,y))
#        y+=1
#    x+=1
#    y=1

for k in move:
    if k=='R' and y<n:
        y+=1
    elif k=='R' and y==n:
        continue
    elif k=='L' and y>1:
        y-=1
    elif k=='L' and y==1:
        continue
    elif k=='U' and x>1:
        x-=1
    elif k=='U' and x==1:
        continue
    elif k=='D' and x==n:
        continue
    elif k=='D' and x<n:
        x+=1

print(x,y)
