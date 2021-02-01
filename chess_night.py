# 왕실의 나이트
input_data = input()
x = int(input_data[1])
y = int(ord(input_data[0])) - int(ord('a')) + 1
move_types = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
cnt = 0

for move in move_types:
    nx = x+move[0]
    ny = y+move[1]

    if nx>8 or ny>8 or nx<1 or ny<1:
        continue
    else:
        cnt+=1

print(cnt)
