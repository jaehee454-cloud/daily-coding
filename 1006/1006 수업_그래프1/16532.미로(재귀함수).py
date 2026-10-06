T = int(input())

# 상하좌우 델타배열
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 이 재귀함수의 단계를 나타내는 값은 하나가 아니라 두개다.
# 현재 미로안의 행번호, 열번호(i,j)
# 행번호와 열번호를 계산해서 그 위치에 3(도착지점)이 있으면 종료
def dfs(i, j, N):
    global answer

    # 3인 곳에 도착하면 바로 종료
    # 1. 종료조건 (기저 조건)
    if maze[i][j] == 3:
        answer = 1
        return

    # (i,j)위치에 있는 노드의 4방향(상하좌우) 탐색후
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        # 2차원 리스트 범위 안, 이전에 방문하지 않았고, 벽이 아니여야 하고
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
            visited[ni][nj] = 1
            # stack.append((i,j))
            # 우리가 만든 스택이 아닌, 파이썬의 함수 호출 구조를 이용한다.
            # 함수 호출구조가 스택과 동일하게 동작(후입선출)하기 때문에..
            dfs(ni,nj,N)

for tc in range(1, T + 1):
    # 미로의 크기
    N = int(input())
    # 미로 정보 (2차원 리스트, 그래프)
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작지점(2) 찾기
    si, sj = 0,0
    for i in range(N):
        for j in range(N):
            # print(i,j,N)
            if maze[i][j] == 2:
                si,sj = i,j
                break

    answer = 0
    # 방문배열 0으로 채워놓고 시작하는 일은 한번만
    visited = [[0] * N for _ in range(N)]
    # 재귀호출 시작
    dfs(si,sj,N)

    print(f"#{tc} {answer}")
"""

3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

"""