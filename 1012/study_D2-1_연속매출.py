# repeat

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    sales = list(map(int, input().split()))

    ans_max = 0
    ans_min = float('inf')
    ans_final = 0

    for i in range(N - M + 1):
        sales_sum = 0
        for j in range(M):
            sales_sum += sales[i + j]
        ans_max = max(ans_max, sales_sum)
        ans_min = min(ans_min, sales_sum)

    ans_final = ans_max - ans_min
    print(f"#{tc} {ans_final}")
