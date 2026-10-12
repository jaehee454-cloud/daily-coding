T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    B = list(map(int, input().split()))

    for i in range(N):
        max_height = 0

        for j in range(1, K+1):
            if B[i-j] > max_height:
                max_height = B[i-j]
                