# 정렬 대상 리스트
arr = [69, 10, 30, 2, 16, 8, 31, 22]

# 분할정복
# 분할 하고 분할한 작은 부분을 정렬
# 합칠때 정렬이 이루어진다.

# m : 우리가 정렬하고싶은 배열(리스트)
def merge_sort(m):

    # 종료 조건 (언제까지 분할 할 것인지)
    if len(m) == 1:
        return m

    # 분할
    # 반으로 쪼개서 왼쪽부분, 오른쪽 부분으로 분할
    mid = len(m) // 2
    # m[: mid] : left
    left = m[:mid]
    # m[mid :] : right
    right = m[mid:]

    # 정복
    left = merge_sort(left)
    right = merge_sort(right)

    # 합병
    return merge(left, right)

# 왼쪽부분과 오른쪽 부분을 합치는 함수
# 합치면서 정렬이 진행된다.
def merge(left, right):

    # 최소값의 위치(left, right 는 이미 정렬이 되어있는 상태)
    li = ri = 0

    result = []

    # 왼쪽에 원소가 남아있거나 오른쪽에 원소가 남아있다면 반복
    while li < len(left) or ri < len(right):
        # 왼쪽과 오른쪽 둘 다 남아 있는경우
        if li < len(left) and ri < len(right):
            # 왼쪽의 최소값과 오른쪽의 최소값 비교해서 더 작은거 선택
            if left[li] <= right[ri]:
                # 왼쪽의 최소값이 더 작았으니까 왼쪽 선택
                result.append(left[li])
                li += 1
            else:
                # 오른쪽의 최소값이 더 작은 경우
                result.append(right[ri])
                ri += 1
        # 왼쪽만 남은 경우 => 비교 대상 없으니까 쭉 이어 써줌
        elif li < len(left):
            result.append(left[li])
            li += 1
        # 오른쪽만 남은 경우
        elif ri < len(right):
            result.append(right[ri])
            ri += 1

    # 위의 while 문을 반복하면서 정렬이 된다.
    return result


print(merge_sort(arr))