T = int(input())


# i : 정류장 번호, 단계
# cnt : 현재 i번 정류장 까지 오는데 충전 횟수
def drive(i, cnt):
    global min_cnt

    # 0. 가지치기
    # 이전에 내가 구한 최소 충전 횟수보다 현재 충전횟수가 같거나 크다면
    # 더이상 진행할 필요가 없다.
    if min_cnt <= cnt - 1:
        return

    # 1. 기저 조건 (종료 조건)
    # 마지막 정류장 (N번 정류장 도착시)
    # 마지막 정류장 뒤로 좀 넘어가도 도착할수 있으니 >= 사용
    if i >= N:
        # 현재 내가 충전한 횟수가 최소값인지 확인하고 갱신
        # 출발지 충전 횟수는 세지 않기로 했으니 - 1
        min_cnt = min(cnt - 1, min_cnt)
        return

    # 2. 재귀 호출
    # 다음 단계로 넘어갈 수 있는 경우의수(branch) 생각
    # 현재 정류장 번호는 i, 현재 정류장의 충전 용량은 bus_stop[i]
    # 우리가 다음에 갈수 있는 거리는 1 ~ bus_stop[i] 까지 가능
    for j in range(bus_stop[i], 0, -1):
        # 충전횟수 + 1, 다음에 갈 정류장 번호는 i+j번
        drive(i + j, cnt + 1)


for tc in range(1, T + 1):
    # 맨 앞 숫자는 N, 정류장 개수
    # 나머지 숫자들은 bus_stop, 각 정류장의 충전지 용량
    N, *bus_stop = map(int, input().split())

    # 정류장 번호 1번부터 시작하도록 인덱스 조정(패딩)
    bus_stop = [0] + bus_stop

    # 문제에서 원하는 답 : 최소 충전 횟수
    min_cnt = 9999999

    # 1번정류장에서 출발, 충전횟수 0번
    drive(1, 0)

    print(f"#{tc} {min_cnt}")