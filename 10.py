x = input()

# 입력받은 x의 행과 열의 값을
# posi_m, posi_n에 넣어준다.
# ※ 참고로 그냥 x[1]하면 str로 여겨지기에 int로 변환해주어야 한다.
posi_m = int(x[1])
# ord를 이용해서 알파벳을 숫자로 바꿔준다.
posi_n = int(ord(x[0])-ord('a')+1)

# 번거로워 보이지만, 각 움직임을 이렇게 move에 넣어준다.
move = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
cnt = 0

for i in move:
    next_posi_m = posi_m + i[0]
    next_posi_n = posi_n + i[1]

    if next_posi_m<0 or next_posi_n<0:
        cnt+=1
        
print(len(move)-cnt)
    
