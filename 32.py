# 이진탐색 -- 시간 복잡도: O(logN)
# 재귀함수를 이용한 방법

def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

print("원소의 개수와 찾고자 하는 숫자를 입력하세요.")
n,target = map(int, input().split())
print("전체 원소를 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array의 자료형은 리스트여야 한다.
# 리스트형으로 해서 길이를 절반씩 줄이면서 진행한다.
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1,"번째에 원소가 존재합니다.")
        
