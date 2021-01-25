# 팀 결성: 서로소 집합 알고리즘 활용

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

print("n과 m 값을 입력하세요. >")
n,m = map(int, input().split())
# 부모 테이블 초기화
parent = [0]*(n+1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(n+1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    print("연산을 입력하세요. >")
    comment, a, b = map(int, input().split())

    # 합집합 연산인 경우
    if comment == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif comment == 1:
        if find_parent(parent,a) == find_parent(parent,b):
            print('Yes')
        else:
            print('No')
