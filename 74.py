# 커리큘럼: 위상정렬
from collections import deque
import copy

print("노드의 개수를 입력하세요. >")
v = int(input())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0]*(v+1)

# 그래프 초기화
graph = [[] for i in range(v+1)]
# 각 시간을 0으로 초기화
time = [0]*(v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    print("간선 정보를 입력하세요. >")
    data = list(map(int, input().split()))
    # 첫 번째 수는 시간 정보를 담고 있음
    time[i] = data[0]
    
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = copy.deepcopy(time)
    q = deque()

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()

        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i]-=1

            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i]==0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()

                
