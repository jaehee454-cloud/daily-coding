# 현재 방번호 : now
# 내가 지금까지 들른 방번호 모음 : visited
# 내가 지금까지 사용한 에너지 사용량 : e

def solve(now, visited, e):
    global answer

    # 모든 방을 다 돌면, 종료
    if len(visited) == N:
        total = e + Energy[now][0]
        answer = min(answer, total)
        return

    # 재귀함수: 0부터 N-1까지 한번씩 방문해야 한다
    for i in range(N):

        if i not in visited:    # 방문 안 했다면, solve 재귀 호출
            # i번 구역으로 이동, i번 방문 목록에 추가, now -> i 에너지 사용량 더하기
            solve(i, visited + [i], e + Energy[now][i])



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Energy = [list(map(int, input().split())) for _ in range(N)]

    answer = 100000

    solve(0, [0], 0)

    print(f"#{tc} {answer}")
