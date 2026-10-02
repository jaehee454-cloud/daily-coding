T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    panel = [list(map(int, input().split())) for _ in range(N)]
    lens = [list(map(int, input().split())) for _ in range(M)]
    new_panel = [[0]*(N-M+1) for _ in range(N-M+1)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            energy = 0
            for ni in range(M):
                for nj in range(M):
                    energy += panel[i+ni][j+nj] + lens[ni][nj]
            new_panel[i][j] = energy

    print(f"#{tc}")
    for row in new_panel:
        print(*row)

