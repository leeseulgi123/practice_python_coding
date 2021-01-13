# 최단경로 복습 1
import sys
input = sys.stdin.readline

INF = int(1e9)

print("노드의 개수와 간선의 개수를 입력하세요.(구분자:띄어쓰기)")
n,m = map(int, input().split())
print("시작 노드를 입력하세요.")
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for _ in range(m):
    print("# _번 노드에서 _번 노드로 가는 비용이 _이다. => 입력하세요.")
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

    def get_smallest_node():
        min_value = INF

        index = 0

        for i in range(1, n+1):
            if distance[i]<min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start):
        distance[start] = 0
        visited[start] = True

        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(n-1):
            now = get_smallest_node()
            visited[now] = True

            for j in graph[now]:
                cost = distance[now]+j[1]

                if cost<distance[j[0]]:
                    distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
