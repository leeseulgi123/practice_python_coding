# 이진탐색
# 반복문을 이용한 방법

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

print("원소의 개수와 찾고자 하는 정수를 입력하세요.")
n, target = map(int, input().split())
print("전체 원소를 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n+1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1, "번째에 원소가 존재합니다.")
