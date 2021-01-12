# 1로 만들기 복습 : 다이나믹 프로그래밍
# 점화식: a(i) = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1
print("정수를 입력하세요.")
x = int(input())

d = [0]*30001

d[0] = 0
d[1] = 0

for i in range(3,x+1):
    d[i] = d[i-1] + 1
    
    if d[i]%5==0:
        d[i] = min(d[i], d[i//5]+1)
    if d[i]%3==0:
        d[i] = min(d[i], d[i//3]+1)
    if d[i]%2==0:
        d[i] = min(d[i], d[i//2]+1)

print(d[x])
    
