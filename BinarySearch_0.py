# 이진트리 복습: 부품찾기(1)
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
    if i in array_a:
        print("Yes", end=' ')
    else:
        print("No", end=' ')
