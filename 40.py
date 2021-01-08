# 피보나치
# 다이나믹 프로그래밍으로 구현(메모이제이션)- 재귀 함수 이용.
# Top-Down 방식

# 메모이제이션?
# 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면
# 메모한 결과를 그대로 가져오는 기법.

# - 다이나믹 프로그래밍 사용 조건
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

d = [0]*100

def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    if d[n] != 0:
        return d[n]

    d[n] = fibonacci(n-1) + fibonacci(n-2)
    return d[n]

print(fibonacci(99))
