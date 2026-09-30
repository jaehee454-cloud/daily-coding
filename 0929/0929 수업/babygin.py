# 6자리 숫자 입력
# level 6, branch 6 재귀함수
numbers = list(map(int, input()))

# i : 단계를 나타낼 파라미터
# path : 각 단계에서 고른 숫자 저장
# 지금까지 만든 순열의 상태를 나타낸다
# used : 각 단계에서 사용한 인덱스 체크

ans = 0
def perm(i, path, used):
    global ans

    # 기저 조건
    if i == 6:  # level 6
        # 순열을 완성한 상태
        # path에서 앞3 / 뒤3 앞 뒤가 각각 run 또는 triplet 이면 baby gin
        print(path)
        if (
                (path[0] == path[1] == path[2]
                 or path[0] + 1 == path[1] and path[1] + 1 == path[2])
                and
                (path[3] == path[4] == path[5]
                 or path[3] + 1 == path[4] and path[4] + 1 == path[5])
        ):
            ans = 1
        return

    # 재귀 호출
    for j in range(6):  # branch 6
        # j : i 단계에서 고를 숫자의 인덱스
        # 이전에 j번 인덱스에 있는 숫자를 사용했는지 확인해야 함
        # 사용했다면 다른 인덱스에 있는 숫자를 사용하도록 건너뛴다.
        if used[j]:
            continue

        # j번 숫자 사용 체크
        # i번 숫자 순열에 넣고
        used[j] = 1
        path.append(numbers[j])
        perm(i+1, path, used)
        # j번 숫자 사용해제
        # j번 숫자 순열에서 제거
        used[j] = 0
        path.pop()

# 0단계부터 시작, 순열 초기 상태(아무것도 선택안함), 사용한 인덱스(아무것도 사용안함)
perm(0, [], [0] * 6)

if ans:
    print("Baby Gin")
else:
    print("Not baby Gin")