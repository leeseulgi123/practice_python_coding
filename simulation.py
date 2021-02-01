# 시뮬레이션 유형
n = int(input())
x = 1
y = 1
plans = input().split()

# L,R,U,D
move_types = [(0,-1),(0,1),(-1,0),(1,0)]
move_names = ['L','R','U','D']

for plan in plans:
    for i in range(4):
        if plan == move_names[i]:
            nx = x+move_types[i][0]
            ny = y+move_types[i][1]

    if nx>n or ny>n or nx<1 or ny<1:
        continue

    x,y = nx,ny


print("이동 후 위치: ", x, y)
            
            
