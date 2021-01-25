# 정렬 복습
a = list(map(int, input().split()))

a.sort(reverse = True)

for i in range(len(a)):
    print(a[i], end = ' ')
