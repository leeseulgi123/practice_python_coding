# 그리디 복습
print("N값과 나눌 숫자를 입력하세요. >")
n,k = map(int, input().split())
cnt = 0

# n값이 1이 아닐 동안 계속 수행.
while n != 1:
    # 만약 n이 1이면 멈춘다.
    if n == 1:
        break
    # n이 k값으로 나누어 지면 나누고, n과 cnt를 갱신.
    if n%k==0:
        n//=k
        cnt+=1
    # n이 k값으로 나누어지지 않으면, 1을 뺀다.
    else:
        n-=1
        cnt+=1

print(cnt)
        

 

