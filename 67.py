# 전보: 다익스트라 알고리즘 문제
print("<전보: 다익스트라 알고리즘 문제>")
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작노드
print("노드의 개수, 간선의 개수, 시작노드를 입력하세요. >")
n,m,start = map(int, input().split())

# 각 노드에 연결된 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
# 최단 거리를 모두 INF로 초기화
distance = [INF]*(n+1)

# 각 간선의 정보를 입력받는다.
for _ in range(m):
    print("각 간선에 대한 정보를 입력하세요. >")
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가는 최단경로는 0으로 설정. 큐에 삽입.
    heapq.heappush(q, (0,start))
    distance[start] = 0

    # 큐가 비어있지 않다면 계속 진행.
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼낸다.
        dist, now = heapq.heappop(q)
        if dist>distance[now]:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist+i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 실행
dijkstra(start)

# 도달할 수 있는 노드의 수
count = 0
# 도달할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    if d!=INF:
        count+=1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1을 출력한다.
print(count-1, max_distance)
