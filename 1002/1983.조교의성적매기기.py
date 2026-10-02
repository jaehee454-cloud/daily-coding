T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    score = [list(map(int, input().split())) for _ in range(N)]

    total_score = []
    S = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(N):

        # 각 학생의 총점을 빈리스트에 저장
        total_score.append(score[i][0]*0.35 + score[i][1]*0.45 + score[i][2]*0.2)

    # K번째 학생의 점수를 target 변수에 저장
    target = total_score[K-1]

    # 총점을 내림차순으로 정렬
    total_score.sort(reverse=True)

    # K번째 학생의 등수 찾기
    rank = total_score.index(target) + 1

    # 동일한 학점 받을 학생들 그룹짓기
    group = N//10
    # S리스트에서 위치 찾기
    idx = (rank-1)//group
    ans = S[idx]

    print(f"#{tc} {ans}")