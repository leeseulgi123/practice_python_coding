# 간단한 다익스트라 알고리즘(복습)
import sys
input = sys.stdin.readline
INF = int(1e9)

# n = 노드 수
# m = 간선 수
n,m = map(int, input().split())
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 확인하는 리스트
visited = [False]*(n+1)
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())

    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    # 먼저 min_value를 무한으로 해준 다음
    min_value = INF
    index = 0

    for i in range(1, n+1):
        if distance[i]<min_value and not visited[i]:
            # 반복문을 통해 계속 값을 적은 값으로 갱신해 나아간다.
            min_value = distance[i]
            # 그리고 그 값을 index로 가져온다.
            index = i

    return index

# 다익스트라 알고리즘
def dijkstra(start):
    # 시작 노드에 대해서는 거리가 0임.
    distance[start] = 0
    # 시작 노드는 방문되어있는 상태임.
    visited[start] = True

    for j in graph[start]:
        distance[j[0]]=j[1]

    for i in range(n-1):
        # 현재 노드에서 가장 최단 거리가 짧은 노드를 꺼낸다.
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost<distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


