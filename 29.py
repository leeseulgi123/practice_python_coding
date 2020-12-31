# 두 배열의 원소 교체 -- sort를 사용X, min(), max() 사용하는 경우 
N,K = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

# 범위를 벗어나면 이를 알리고, 멈춘다.
if len(array_a) != N or len(array_b) != N:
    print("You have to wirte the array which length is N")
    

for i in range(K):
    min_a = min(array_a)
    array_a.remove(min_a)
    
    max_b = max(array_b)
    array_b.remove(max_b)

    array_a.append(max_b)


print(sum(array_a))
    
    
    
