# 먼저 sort로 정렬하고 진행하는 경우.
N,K = map(int, input().split())

array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

if len(array_a)!=N or len(array_b)!=N:
    print("You have to write the array which length is N.")

array_a.sort()
array_b.sort(reverse = True)

for i in range(K):
    # array_a에 있는 데이터보다 array_b에 있는 원소가 큰 경우에만
    # 스와프한다.
    if array_a[i]<array_b[i]:
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:
    # 아닌 경우에는 멈춘다.
        break

print(sum(array_a))
    
