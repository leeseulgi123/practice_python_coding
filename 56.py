# 플로이드 워셜 알고리즘 복습
INF = int(1e9)

print("노드의 개수를 입력하세요.>")
n = int(input())
print("간선의 개수를 입력하세요.>")
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    print("# _번 노드에서 _번 노드로 가는 비용은 _입니다.>")
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end =' ')
        else:
            print(graph[a][b], end =' ')
    print()
            
