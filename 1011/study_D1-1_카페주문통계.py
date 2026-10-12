# repeat

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    menu = list(map(int, input().split()))

    count = [0] * 101
    max_count = 0
    max_menu = 0

    for i in range(N):
        count[menu[i]] += 1

    for i in range(1, 101):
        if count[i] > max_count:
            max_count = count[i]
            max_menu = i

    print(f"#{tc} {max_menu} {max_count}")