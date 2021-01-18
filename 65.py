# 플로이드 워셜(복습)
INF = int(1e9)

n = int(input())
m = int(input())

x,y = map(int, input().split())

# 2차원 리스트(그래프)
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 거리는 0으로 한다.
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받는다.
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')

    print()

print(x,"에서 ", y,"로 가는 최단경로: ")
print(graph[x][y])
