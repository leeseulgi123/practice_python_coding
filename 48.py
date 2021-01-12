# 개미 전사 복습 : 다이나믹 프로그래밍
n = int(input())
array = list(map(int, input().split()))

d = [0]*100
d[0] = array[0]
d[1] = max(array[0], array[1])

for j in range(2,n):
    d[j] = max(d[j-1], d[j-2] + array[j])
        

print(d[n-1])
