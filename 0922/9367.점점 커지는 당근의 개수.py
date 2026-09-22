T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carr = list(map(int, input().split()))

    cnt = 1
    m = 1       # 구간의 최소 길이는 1
    for i in range(N-1):
        if carr[i+1] - carr[i] >= 1:   # 차이가 1이상의 경우도 고려해야 한다  # carr[i+1] > carr[i]:
            cnt += 1
            m = max(cnt, m)     # cnt 중 큰 값을 m에 저장
        else:           # 연속이 끊기면 cnt는 다시 1
            cnt = 1

    print(f"#{tc} {m}")
