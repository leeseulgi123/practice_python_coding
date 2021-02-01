# 그래프 이론 복습: 커리큘럼
from collections import deque
import copy

print("듣고 싶은 강의의 개수를 입력하세요. >")
v = int(input())
indegree = [0]*(v+1)

graph = [[]for i in range(v+1)]
time = [0]*(v+1)

print("강의 시간과 선수강의 번호를 입력하세요. >")
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i]+=1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i],"시간")

topology_sort()
