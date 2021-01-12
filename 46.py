# 피보나치 : 다이나믹 프로그래밍 복습
d = [0]*100

d[1] = 1
d[2] = 1

n = int(input())

for i in range(3,n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])
