T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for ni in range(M):
                for nj in range(M):
                    fly += arr[i+ni][j+nj]
            ans = max(ans, fly)

    print(f"#{tc} {ans}")

