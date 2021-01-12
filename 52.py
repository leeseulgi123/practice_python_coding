import heapq
import sys

iput = sys.stdin.readline
INF = int(1e9)

print("노드의 개수와 간선의 개수를 입력하세요.(구분자는 띄어쓰기 입니다.)")
n,m = map(int, input().split())
print("시작 노드를 입력하세요.")
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    print("_번 노드에서 _번 노드로 가는 비용이 _이다. => 입력하세요")
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    # 큐가 비어있지 않다면,
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시한다.
        if distance[now]<dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인한다.
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행한다.
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력한다.
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한이라고 출력한다.
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력한다.
    else:
        print(distance[i])
    
