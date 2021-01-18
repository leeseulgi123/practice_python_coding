# 개선된 다익스트라 알고리즘 소스코드(복습)
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 큐에 시작 노드로 가기 위한 최단 경로는 0이라고 삽입.
    heapq.heappush(q, (0,start))
    distance[start] = 0

    # 큐가 비어있지 않다면,
    while q:
        dist, now = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있다면 무시.
        if dist > distance[now]:
            continue

        # 현재 노드와 연결된 인접 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]

            # 현재 노드를 거쳐서 나른 노드로 이동하는 거리가 더 짧은 경우.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
