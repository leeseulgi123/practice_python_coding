# 퀵 정렬(파이썬을 장점을 살린, 기억하기 쉬운 버전)
# -- 평균 시간 복잡도: O(NlogN)
# 그러나 최악의 경우에는 O(N^2)
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array)<=1:
        return array

    # pivot은 첫 번째 원소
    pivot = array[0]
    # pivot을 제외한 원소들을 담은 리스트
    tail = array[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x<=pivot]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x>pivot]

    # 왼쪽 부분을 정렬, 오른쪽 부분 정렬해서, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
