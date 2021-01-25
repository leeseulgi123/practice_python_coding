# 정렬 복습
n = int(input())
mid = []

for i in range(n):
    x = input().split()
    mid.append((x[0],x[1]))

# sorted에서 key = lambda를 잘 활용하기
mid = sorted(mid, key = lambda y:y[1])

for y in mid:
    print(y[0], end = ' ')



    
    
