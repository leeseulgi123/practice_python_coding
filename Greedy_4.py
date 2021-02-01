# 그리디 복습
n = int(input())
cnt = 0

types = [500,100,50,10]

for coin in types:
    cnt+=n//coin
    n%=coin

print("필요한 동전의 개수(최솟값):")
print(cnt)
