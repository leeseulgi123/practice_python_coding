N = int(input())
food = list(map(int, input().split()))

if len(food) != N:
    print("식량의 정보가 잘못 되었습니다.")

d = [0]*100

d[0] = food[0]
d[1] = max(food[0],food[1])

for i in range(2,N):
    # (i)번째 식량 == 현재 식량
    
    # (i-1)번째 식량을 털면 현재 식량을 털 수 없다.
    # (i-2)번째 식량을 털면 현재 식량을 털 수 있다.
    # => 결과적으로 이 중 큰 것을 고르면 된다.
    d[i] = max(d[i-1], d[i-2]+food[i])

print(d[N-1])

