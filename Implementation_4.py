# 구현 복습
print("지도의 크기를 입력하세요.(행,열) >")
n,m = map(int, input().split())

print("현재 캐릭터의 위치(행,렬)와 방향을 입력하세요. >")
x,y,d = map(int, input().split())

cnt = 1
turn_time = 0

# 경로
#(왼, 오, 상, 하)
steps = [(0,-1),(0,1),(-1,0),(1,0)]

# 방향
#(북, 동, 남, 서)
directions = [(-1,0),(0,1),(1,0),(0,-1)]

# 방문한 위치를 저장하는 2차원 리스트
my_path = [[0]*m for _ in range(n)]

# 시작한 위치는 방문처리
my_path[x][y] = 1

# 맵의 행, 열의 정보를 담는 리스트
my_map = []
print(str(n)+"행의"+" 맵 정보를 입력하세요. >")
for i in range(n):
    my_map.append(list(map(int, input().split())))

# 왼쪽으로 회전시켜주는 함수
# (d값이 -1되면 3으로 처리한다.)
def turn_left():
    global d
    d -= 1
    
    if d==-1:
        d = 3

while True:
    # 우선적으로 왼쪽 회전을 수행.
    turn_left()
    nx = x+directions[d][0]
    ny = y+directions[d][1]

    # 정면에 가보지 않은 칸이 존재하면 이동.
    if my_path[nx][ny] == 0 and my_map[nx][ny] == 0:
        # 우선 방문처리. 
        my_path[nx][ny] = 1
        # 캐릭터의 현재 위치를 갱신한다. 
        x,y = nx,ny
        # 이동 횟수 1 증가 
        cnt+=1
        turn_time = 0
        continue
    
    # 정면에 있는 공간에 방문한 적 있으면, 
    else:
        # 한번 턴.
        turn_time+=1
        
    # 만약 4 방향을 모두 가봤으면,  
    if turn_time == 4:
        nx = x+directions[d][0]
        ny = y+directions[d][1]
        # 땅이면 이동
        if my_map[nx][ny] == 0:
            x = nx
            y = ny
            
        # 바다이면 멈춤
        else:
            break

        turn_time = 0

print("캐릭터는 총 "+str(cnt)+"칸을 방문했습니다.")
        
        
        

    




    
