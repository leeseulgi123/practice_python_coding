# BFS 복습
# 괴물 있으면 0, 괴물 없으면 1

from collections import deque

print("행과 열의 개수를 입력하세요. >")
n,m = map(int, input().split())

graph = []

print("맵 정보를 입력하세요. >")
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS 함수
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌때까지 계속
    while queue:
        x,y = queue.popleft()

        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 범위 벗어나면 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 괴물 있으면 무시
            if graph[nx][ny] == 0:
                continue
            # 괴물 없으면 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))
