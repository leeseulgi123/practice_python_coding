# DFS 복습
print("행과 열의 개수를 입력하세요. >")
n,m = map(int, input().split())

print("그래프 정보를 입력하세요. >")
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    # 범위를 벗어나면 False
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 방문하지 않은 곳이라면
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 재귀를 이용하여 상하좌우 영역도 확인
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0

# 모든 노드에 음료수를 채운다
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print("만들 수 있는 아이스크림의 개수: ")
print(result)
