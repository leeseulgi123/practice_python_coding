# 정렬 복습
n,k = map(int, input().split())

print("배열 a를 입력하세요. >")
a = list(map(int, input().split()))

print("배열 b를 입력하세요. >")
b = list(map(int, input().split()))

if len(a) != n or len(b) != n:
    print("잘못된 길이의 배열을 입력했습니다.")

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
    
