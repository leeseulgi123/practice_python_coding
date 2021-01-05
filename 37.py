# 계수정렬을 이용한 방법
print("슬기네 전자 매장의 부품 개수를 입력하세요.")
n = int(input())
print("보유한 부품 번호를 입력하세요. 구분은 띄어쓰기 입니다.")
array_n = [0]*1000001

for i in input().split():
    array_n[int(i)] = 1

print("손님이 문의한 부품 개수를 입력하세요.")
m = int(input())
print("손님이 문의한 부품 번호를 입력하세요. 구분은 띄어쓰기 입니다.")
array_m = list(map(int, input().split()))

for i in array_m:
    if array_n[i]==1:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')
