T = int(input())

for tc in range(1, T+1):
    N = int(input())
    K = list(map(int, input().split()))

    ans = 1
    for i in range(N-1):
        if K[i] <= K[i+1]:
            ans = 0
            break
    print(f"#{tc} {ans}")