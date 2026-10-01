T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split())) # 정렬대상
    B = list(map(int, input().split())) # 검색대상

    cnt = 0

    A.sort()

    for i in B:
        left = 0
        right = N -1
        # 내가 이전에 선택한 방향, 처음은 -1로, 왼쪽은 0, 오른쪽은 1로
        D = -1

        while left <= right:
            mid = (left + right) // 2
            if  A[mid] == i:
                # 찾음
                cnt += 1
                break

            elif A[mid] > i:
                # 왼쪽 방향 선택
                right = m - 1
                # 내가 만약 이전에도 왼쪽을 선택했다면, 조건위반
                if D == 0:
                    break
                else:
                    D = 0
            else:
                left = mid + 1
                if D == 1:
                    break
                else:
                    D = 1

    print(f"#{tc} {cnt}")