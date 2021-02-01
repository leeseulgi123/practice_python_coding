graph = [[] for _ in range(3)]

# 노드 0에 1번 노드가 거리 7로 연결
graph[0].append((1,7))
# 노드 0에 2번 노드가 거리 5로 연결
graph[0].append((2,5))
# 노드 1에 0번 노드가 거리 7로 연결
graph[1].append((0,7))
# 노드 2에 0번 노드가 거리 5로 연결
graph[2].append((0,5))

print(graph)
