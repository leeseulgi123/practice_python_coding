# map 사용했더니 에러남.
# 그래서 int(input())으로 함.
N = int(input())

mid = []

for _ in range(N):
    x = int(input())
    mid.append(x)

mid = sorted(mid, reverse = True)

for i in range(N):
    print(mid[i], end=' ')

