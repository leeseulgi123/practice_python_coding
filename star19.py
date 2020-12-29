from collections import deque

# 행과 열 정보 입력받기.
n,m = map(int, input().split())

graph = []
# 그래프 정보 입력받기. -> 리스트로 받기!
for i in range(n):
    graph.append(list(map(int, input())))


# DFS 함수를 만들어서 해결하자.
def dfs(x,y):
    # 우선, 주어진 행과 열을 벗어나는 경우에 종료하도록 한다.
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # graph의 원소가 0이면..
    if graph[x][y] == 0:
        # 방문처리를 하고,
        graph[x][y] = 1
        # 재귀를 이용하여 상,하,좌,우에 인접한 지점을 살펴보며
        # 값이 아직 0이고, 방문하지 않았으면 방문처리한다.
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    #이미 방문한 곳이라면 False.
    return False

cnt = 0
# graph의 모든 노드에 대하여 True인 지점이 보이면
# cnt+=1 한다.
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt+=1

print(cnt)
        



