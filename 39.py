# 피보나치 함수 -- 시간 복잡도: O(2^N)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))
