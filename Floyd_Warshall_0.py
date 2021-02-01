# 최단경로 복습: 미래 도시
# n에서 k를 거쳐 x로 가는 최단 경로
INF = int(1e9)

print("노드의 개수와 간선의 개수를 입력하세요. >")
n,m = map(int, input().split())
# 2차원 리스트,즉 그래프를 만들고 모든 원소 값을 무한으로 초기화.
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 향하는 비용은 0으로 초기화.
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선에 대한 정보를 입력받고 비용은 1로 초기화.
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
print("거쳐갈 노드 k와 도착지 x를 입력하세요. >")
x,k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


distance = graph[1][k] + graph[k][x]

if distance>=INF:
    print("-1")
else:
    print(distance)
