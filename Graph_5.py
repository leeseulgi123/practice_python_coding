# 그래프 이론 복습: 팀 결성

# 루트 노드(parent) 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
# a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

print("0번부터 n번까지의 번호를 부여하고, m번의 연산을 수행한다.")
print("n,m 값을 입력하세요.")
n,m = map(int, input().split())
parent = [0]*(n+1)

for i in range(0, n+1):
    parent[i] = i

print("-----------------------------------------------")
print("연산을 입력하세요.")

for i in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("Yes")
        else:
            print("No")
