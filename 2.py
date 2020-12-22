def solution(N):
    money_list = [500,100,50,10]
    cnt = 0

    for money in money_list:
        cnt+=N//money
        N%=money
    return cnt

print(solution(500))
print(solution(1200))
print(solution(1350))
