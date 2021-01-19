# 미래도시: 플로이드 워셜 알고리즘 문제
print("미래도시: 플로이드 워셜 알고리즘 문제")
INF = int(1e9)

# n: 노드의 개수, m: 간선의 개수
print("노드의 개수와 간선의 개수를 입력하세요. >")
n,m = map(int, input().split())
# 2차원 리스트를 만들고, 모든 값을 INF로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 향하는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] == 0

# 각 간선에 대한 정보를 입력받는다.
for _ in range(m):
    print("각 간선의 정보를 입력하세요. >")
    a,b = map(int, input().split())
    # 양방향으로 이동이 가능하며 모두 비용은 1만큼 든다.
    graph[a][b] = 1
    graph[b][a] = 1

# x: 소개팅할 노드(거쳐갈 노드임), k: 최종 도착지 노드 
print("소개팅할 노드(거쳐갈 노드)와 최종 도착지 노드를 입력하세요. >")
x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 1에서 x를 거쳐 최종 도착지 k로 가는 최단경로
distance = graph[1][x]+graph[x][k]

if distance>=INF:
    print("-1")
else:
    print(distance)


    
