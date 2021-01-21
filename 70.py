# 크루스칼 알고리즘
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

print("노드의 개수와 간선의 개수를 입력하세요. >")
v,e = map(int, input().split())
parent = [0]*(v+1)
# 모든 간선을 담을 리스트와 최종 비용
edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    print("각 간선과 이에 대한 비용을 입력하세요. >")
    a,b,cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
print(result)
