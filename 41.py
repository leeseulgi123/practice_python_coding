# 피보나치
# 반복문을 이용한 다이나믹 프로그래밍
# Bottom-Up 방식(전형적인 방법)

d = [0]*100

d[1] = 1
d[2] = 1
n = 99

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])
