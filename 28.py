N = int(input())

array = []

for _ in range(N):
    # 일단 입력을 받고,
    input_data = input().split()
    # ★ (input_data[0],input_data[1]) 형태로 배열에 append한다. 
    array.append((input_data[0], input_data[1]))

# sorted에서 key에는 함수가 들어간다. lambda 활용함.
result = sorted(array, key = lambda data : data[1])

for i in range(N):
    print(result[i][0], end = ' ')
