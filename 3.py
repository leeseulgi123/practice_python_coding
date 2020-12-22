n, m, k = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
cnt = 0

# sort()를 활용해서
data.sort()

# 미리 가장 큰 값과 두 번째로 큰 값을 정해두기.
first = data[-1]
second = data[-2]

while True:
    # k번 최댓값을 더한다.
    for i in range(k):
        # 우선 m = 0 인지 확인한다.
        if m == 0:
            break
        answer+=first
        m-=1

    # 우선 m = 0 인지 확인한다.
    if m == 0:
        break
    # k번 다 더했으면 이제, 두 번째로 큰 값을 더한다.
    answer+=second
    m-=1

print(answer)
