# 선택 정렬 --  시간 복잡도 O(N^2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    # 일단 맨 앞에 있는 것을 min_index로 둔다.
    # for 문에 의해 그 다음엔 두번째 값이 min_index가 된다.
    min_index = i
    # i의 뒤에 있는 인덱스들 중에서
    # 가장 작은 인덱스를 min_index로 바꿔준다.
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index = j
    # 스와프 한다.
    # 즉, array[i]에 array[min_index]를 두고
    # array[min_index]가 있던 자리에 array[i]를 둔다.
    array[i], array[min_index] = array[min_index], array[i]

print(array)
            
