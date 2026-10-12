# repeat

T = int(input())

for tc in range(1, T+1):
    N, D = map(int, input().split())
    B = list(map(int, input().split()))

    ans = 0
    for i in range(D):
        if max(B) - min(B) <= 1:
            break

        max_idx = B.index(max(B))
        B[max_idx] -= 1

        min_idx = B.index(min(B))
        B[min_idx] += 1

    ans = max(B) - min(B)

    print(f"#{tc} {ans}")
