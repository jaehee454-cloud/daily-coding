T = int(input())

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j):
    visited[i][j] = True

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] == "L" and not visited[ni][nj]:
                dfs(ni, nj)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    cnt = 0
    # 이중for문으로 "L"찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "L" and not visited[i][j]:  # "L"발견
                cnt += 1
                dfs(i, j)   # dfs함수를 호출해, 주변에 다른 "L"이 없는지 확인

    print(f"#{tc} {cnt}")