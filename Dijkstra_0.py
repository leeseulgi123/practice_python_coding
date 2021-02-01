# 최단경로 복습: 전보
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

print("노드의 개수, 간선의 개수, 시작 노드를 입력하세요. >")
n,m, start = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담을 리스트
graph = [[] for i in range(n+1)]
# 최단거리 테이블을 무한으로 초기화 
distance = [INF] *(n+1)

print("간선에 대한 정보를 입력하세요. >")
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    # 시작 노드로 가는 최단경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보를 꺼낸다.
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        # 현재 노드와 인접한 다른 노드들을 확인한다.
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우.
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드이면
    if d != INF:
        cnt+=1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)
