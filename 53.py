# 플로이드 워셜 알고리즘
INF = int(1e9)

print("노드의 개수를 입력하세요.")
n = int(input())
print("간선의 개수를 입력하세요.")
m = int(input())

# 이차원 리스트를 만들고, 모든 값을 무한으로 초기화.
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에게 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    print("_번 노드에서 _번 노드로 가는 비용은 _입니다. => 입력하세요.")
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 위셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한이라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 경우, 거리를 출력
        else:
            print(graph[a][b], end=' ')
    print()
