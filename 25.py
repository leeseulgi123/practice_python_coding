# 계수 정렬 -- 최악의 경우에도 시간 복잡도: O(N+K)
# 다만 처리할 수 있는 정수의 수에 제한이 있는편...
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
mid = []
# 모든 범위를 포함하는 리스트 선언
cnt = [0]*(max(array)+1)

# 각 데이터에 해당하는 인덱스의 값을 1씩 증가.
for i in range(len(array)):
    cnt[array[i]]+=1

# 리스트에 기록된 정렬 정보에서
for i in range(len(cnt)):
    # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스를 출력.
    for j in range(cnt[i]):
        mid.append(i)
mid = set(mid)
print(mid)

