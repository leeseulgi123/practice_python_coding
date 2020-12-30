# sorted와 key를 활용한 소스코드
array = [('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

# key값에는 함수가 들어가야 한다.
result = sorted(array, key = setting)
print(result)
