# 이진트리 복습: 부품찾기(2)
def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end)//2

        # 찾으면 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점 값보다 작으면, 중간점의 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        # 중간점 값보다 크면, 중간점의 오른쪽 확인
        else:
            start = mid+1
    
print("매장에 있는 부품의 개수를 입력하세요. >")
n = int(input())
print("부품 번호를 입력하세요. >")
array_a = list(map(int, input().split()))

print("손님이 문의한 부품의 개수를 입력하세요. >")
m = int(input())
print("부품 번호를 입력하세요. >")
array_b = list(map(int, input().split()))

if len(array_a) != n or len(array_b) != m:
    print("잘못된 입력입니다.")

for i in array_b:
    result = binary_search(array_a, i, 0, n-1)

    if result != None:
        print("Yes", end=' ')
    else:
        print("No", end=' ')
