# 퀵 정렬(정통방식)
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start>=end:
        return
    # 첫번째 원소를 pivot으로.
    pivot = start
    left = start+1
    right = end

    while left<=right:
        # pivot보다 큰 데이터를 찾을 때까지 반복.
        while left<=end and array[left]<=array[pivot]:
            left+=1
        # pivot보다 작은 데이터를 찾을 때까지 반복.
        while right>start and array[right]>=array[pivot]:
            right-=1

        # 엇갈렸다면,
        if left>right:
            # 작은 데이터와 pivot을 스와프
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면,
        else:
            # 작은 데이터와 큰 데이터를 스와프
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)
