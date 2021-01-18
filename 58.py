# 다이나믹 프로그래밍: 반복을 활용한 재귀함수

d = [0]*100

def fibo(x):
    d[1]=1
    d[2]=1

    for i in range(3,x+1):
        d[i] = d[i-1]+d[i-2]

    return d[i]

print(fibo(99))
