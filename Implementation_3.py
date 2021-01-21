# 구현 복습:implementation_0의 다른 버전.
print("(정사각형 모양)지도의 한 변의 길이를 입력하세요. >")
n = int(input())
print("경로를 입력하세요. >")
paths = input().split()

# x값과 y를 1로 초기화
x,y = 1,1

# 경로의 종류
types = ['L', 'R', 'U', 'D']
# 경로에 따른 위치 변화
steps = [(0,-1),(0,1),(-1,0),(1,0)]

# 입력한 경로들을 하나씩 살펴본다.
for path in paths:
    # 경로의 종류 4가지 중에서
    for i in range(4):
        # 경로가 type[i]이면,
        if path == types[i]:
            # x를 x+dx[i]로 갱신(nx)
            nx=x+steps[i][0]
            # y를 y+dy[i]로 갱신(ny)
            ny=y+steps[i][1]
    # 만약 경로를 벗어나면 무시한다.
    if nx<1 or nx>n or ny<1 or ny>n:
        continue
    # 이동을 수행한다.
    x,y = nx, ny
    
print(x,y)
    
    
