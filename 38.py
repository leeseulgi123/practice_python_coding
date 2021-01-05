# 이진탐색 예제
n,m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진탐색을 위한 시작점과 끝점
start = 0
end = max(array)

# 이진탐색 시작
result = 0

while(start<=end):
    total = 0
    mid = (start+end)//2

    for i in array:
        if i>mid:
            total += i-mid

    # 총 떡의 길이가 너무 작으면, 너무 많이 잘라낸 것이기에
    # 절단기의 높이를 줄인다.
    if total<m:
        end = mid-1
    # 총 떡의 길이가 너무 길면, 너무 조금 잘라낸 것이기에
    # 절단기의 높이를 늘린다.
    else:
        # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록.
        result = mid
        start = mid+1

print(result)
        
