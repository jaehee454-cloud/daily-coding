T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carr = list(map(int, input().split()))

    # 구간의 최소 길이는 1이기에, 기본값 cnt = 1로 설정
    cnt = 1
    m = 1
    for i in range(N-1):
        if carr[i] < carr[i+1]:
            cnt += 1
            m = max(cnt, m)
        else:
            cnt = 1

    print(f"#{tc} {m}")