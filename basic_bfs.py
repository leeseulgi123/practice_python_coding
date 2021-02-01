from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print("노드의 개수를 입력하세요.>")
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False]*n

bfs(graph, 1, visited)
