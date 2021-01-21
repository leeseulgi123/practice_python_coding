# 구현 복습
print("시간을 입력하세요. >")
n = int(input())

cnt = 0

# 시
for i in range(n+1):
    # 분
    for j in range(60):
        # 초
        for k in range(60):
            # 시+분+초 안에 3이 들어있으면 cnt+=1한다.
            if '3' in str(i)+str(j)+str(k):
                cnt+=1

print(cnt)
