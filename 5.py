n,m = map(int, input().split())

mid = []

# 입력을 받아 한 행씩 리스트로 만든다.
# 리스트 형태이기에 min을 사용하여
# mid라는 빈 리스트에 추가해준다.

for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    mid.append(min_data)

# 결과적으로 mid에서 가장 큰 값을 출력한다.
print(max(mid))
