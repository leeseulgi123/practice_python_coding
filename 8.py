# 좀더 깔끔한 풀이.

n = int(input())
x,y = 1,1
move = input().split()
move_types = ['L','R','U','D']

# L,R,U,D
# 이전 코드처럼 보이는대로 각각 if문으로 처리하는 것이 아니라
# 리스트로 미리 계산을 일부분 작성해둔다.
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for m in move:
    for i in range(len(move_types)):
        if m == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y = nx, ny

print(x,y)
