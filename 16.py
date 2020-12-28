# 인접 리스트로 그래프 표현.
# 3개의 노드가 존재 -> 3개의 행으로 구성
# 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# (노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)
