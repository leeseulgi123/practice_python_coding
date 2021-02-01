def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

print("노드의 개수를 입력하세요.>")
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [False]*9

dfs(graph,1,visited)

