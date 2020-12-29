from collections import deque

n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향 정의.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 큐 구현.
    queue = deque()
    # (0,0)에서 시작.
    queue.append((x,y))

    # 큐가 빌 때까지 반복.
    while queue:
        x,y = queue.popleft()

        # 현재 위치에서 인접한 네 방향 확인.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 주어진 범위에서 벗어나면 무시.
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 0이면 즉, 괴물이 있으면 무시.
            if graph[nx][ny] == 0:
                continue
            # 1이면 즉, 괴물이 없고 처음 방문하는 칸이면
            # 지금까지 이동한 칸의 수에 +1 한다.
            # 최단 거리를 기록하는 것이다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환.
    return graph[-1][-1]

print(bfs(0,0))
                
        
        
