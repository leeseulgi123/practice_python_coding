# 이진탐색 복습: 떡볶이 떡 만들기
print("떡의 개수와 손님이 요청한 떡 길이를 입력하세요. >")
n,m = map(int, input().split())
print("떡의 개별 높이를 입력하세요. >")
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while(start<=end):
    total = 0
    # 0과 max(array)의 중간값을 절단기 길이로 정한다.
    mid = (start+end)//2

    for x in array:
        # array의 원소가 절단기보다 길면 자른다.
        if x>mid:
            total+=x-mid
        # 아니면 무시한다.
        else:
            continue
        
    # 요청한 떡보다 부족한 경우(더 작은 절단기 사용해야 한다.)
    if total<m:
        end = mid-1
    # 떡이 충분한 경우(더 큰 절단기 사용해도 ok)
    else:
        # result 값 갱신
        result = mid
        start = mid+1

# 절단기의 최댓값을 구해야 하기 때문에
print(result)


