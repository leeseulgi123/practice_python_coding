# [큰 수 더하기]의 좀 더 효율적인 방법
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

count = m//(k+1)*k
count += m%(k+1)

answer = 0
answer += (count)*first
answer += (m-count)*second

print(answer)
