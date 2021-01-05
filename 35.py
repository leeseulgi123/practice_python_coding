# 집합 자료형을 이용한 방법

print("슬기네 전자 매장의 부품 개수를 입력하세요.")
N = int(input())
print("보유한 부품 번호를 입력하세요. 구분은 띄어쓰기 입니다.")
array_n = list(map(int, input().split()))
print("손님이 문의한 부품 개수를 입력하세요.")
M = int(input())
print("손님이 문의한 부품 번호를 입력하세요. 구분은 띄어쓰기 입니다.")
array_m = list(map(int, input().split()))

for i in array_m:
    if i in array_n:
        print("Yes ", end = '')
    else:
        print("No ", end = '')


    

