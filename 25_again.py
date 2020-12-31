# 계수 정렬 복습
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
mid = []

cnt = [0]*(max(array)+1)

for i in range(len(array)):
    cnt[array[i]]+=1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        mid.append(i)

mid = set(mid)
print(mid)
    
