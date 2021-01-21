# 그리디 복습
print("배열의 크기, 더해지는 횟수, 제한된 연속 횟수를 입력하세요. >")
n,m,k = map(int, input().split())

print("데이터를 입력하세요.(구분자는 띄어쓰기) >")
data = list(map(int, input().split()))
# 일단 쉽게 정렬해둔다.
data.sort()

# 가장 큰 수
first = data[-1]
# 두 번째로 큰 수
second = data[-2]

# 결과는 0으로 초기화
result = 0

while True:
    # 가능한 만큼 연속적으로 더해준다. 
    for i in range(k):
        # m이 0이면 멈춘다.
        if m == 0:
            break
        # 아니면, 가장 큰 값을 더해준다.
        result+=first
        # 그리고 m을 1씩 감소.
        m-=1
    # 만약 m이 0이면 멈춘다.
    if m == 0:
        break
    # 아니면, 두 번째로 큰 값을 더해준다.
    result+=second
    # 그리고 m을 1씩 감소.
    m-=1

print(result)
