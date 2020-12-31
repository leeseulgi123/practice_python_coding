# dfs 복습2

def dfs(x,y):
    # 범위에 해당되지 않으면,
    # False
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    # 얼음칸이 비어있으면, 
    if graph[x][y] == 0:
        # 방문 처리하고,
        graph[x][y] = 1
        # 재귀를 이용해서 상,하,좌,우의 지점을 살피며
        # 비어있는 얼음칸을 방문 처리한다.
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    # 이미 방문한 곳이면 False
    else:
        return False

n,m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt+=1

print(cnt)

