# 이진탐색을 이용한 방법

def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid

        elif array[mid]<target:
            start = mid+1

        else:
            end = mid-1

    return None

print("슬기네 전자 매장의 부품 개수를 입력하세요.")
n = int(input())
print("보유한 부품 번호를 입력하세요. 구분은 띄어쓰기 입니다.")
array_n = list(map(int, input().split()))
# 이진탐색을 수행하려면 정렬되어있어야 한다.
array_n.sort()
print("손님이 문의한 부품 개수를 입력하세요.")
m = int(input())
print("손님이 문의한 부품 번호를 입력하세요. 구분은 띄어쓰기 입니다.")
array_m = list(map(int, input().split()))

for i in array_m:
    result = binary_search(array_n, i, 0, n-1)

    if result != None:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')
