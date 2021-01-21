# 그리디 복습
n,m = map(int, input().split())

mid = []
result = 0

# 일단 총 n행의 카드에 대한 정보를 입력받는다.
for i in range(n):
    cards = map(int, input().split())
    # 그 행에서 가장 작은 값을 mid에 담는다.
    mid.append(min(cards))

    # 결과값을 mid 안의 원소들 중 최댓값으로 갱신한다.
    result = max(mid)

print(result)    
