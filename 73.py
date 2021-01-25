# 도시 분할 계획: 최소 신장 트리
# 크루스칼 알고리즘으로 구하고, 가장 비용이 큰 간선을 제거.

def find_parent(parent, x):
    if parent[x] != x:
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

# 모든 간선을 담을 리스트
edges = []
# 최종 비용을 담을 변수
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
# 최종 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선
last = 0

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
        last = cost

print("유지비의 합(최솟값):")
print(result-last)
        
