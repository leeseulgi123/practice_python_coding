# 바닥 공사 복습 : 다이나믹 프로그래밍
# 점화식 : a(i) = a(i-1) + a(i-2)*2
n = int(input())

d = [0]*1001

d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1]+2*d[i-2])%796796

print(d[n])