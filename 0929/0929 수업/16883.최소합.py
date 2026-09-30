di = [0,1]
dj = [1,0]

def solve(i,j, now_sum):
    global answer

    # 기저조건: 맨 오른쪽 아래에 도착시 종료
    if (i,j) == (N-1, N-1):
        answer = min(answer, now_sum)
        return

    # 재귀호출: 오른쪽, 아래쪽 이동
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]

        if is_valid(ni,nj):
            solve(ni, nj, now_sum + arr[ni][nj])

# 범위 확인 함수
def is_valid(i, j):
    return 0<= i < N and 0 <= j < N


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 10000

    solve(0,0,arr[0][0])

    print(f"#{tc} {answer}")
