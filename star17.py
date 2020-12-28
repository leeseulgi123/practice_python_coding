# DFS 예제

def dfs(graph,v,visited):
    # 현재 노드를 방문처리한다.
    visited[v] = true
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문한다.
    for i in graph[v]:
        # i가 방문하지 않은 노드라면 dfs 함수 재귀적으로 실행.
        if not visited[i]:
            def(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

dfs(graph, 1, visited)
    
