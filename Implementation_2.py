# 구현 복습
# 왕실 정원은 8*8의 크기를 갖는다.
print("나이트의 현재 위치를 입력하세요. >")
data = input()
row = int(data[1])
# 알파벳은 정수로 변환해준다.
column = int(ord(data[0])) - int(ord('a')) + 1

# 각 스탭에 대한 정보.(8가지)
steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

cnt = 0

for step in steps:
    # 현재 행 값을 갱신
    next_row = row+step[0]
    # 현재 열 값을 갱신
    next_column = column+step[1]

    # 해당 이동의 결과가 정상적이면 cnt+=1한다.
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        cnt+=1
    else:
        continue
print(cnt)
