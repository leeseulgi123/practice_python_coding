N = int(input())

d = [0]*1001

# 타일 크기가 1*2이면 : 경우의 수 1가지
d[1] = 1
# 타일 크기가 3*2이면 : 경우의 수 3가지
d[2] = 3

for i in range(3,N+1):
    # d[i-1]까지 채워져 있으면 (2*1) 덮개로 채우는 1가지 경우만 있다.
    # d[i-2]까지 채워져 있으면 (1*2) 덮개 2개 또는 (2*2) 덮개 1개로 채우는
    # 2가지 경우가 있다.

    # 나머지는 고려하지 않아도 된다.
    # Why?
    # 덮개의 형태가 최대 (2*2)이기 때문이다.

    # % 796796은 그냥 숫자가 너무 커짐을 방지하기 위함이다.
    d[i]= (d[i-1] + 2*d[i-2])%796796

print(d[N])
