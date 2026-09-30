# 테스트케이스 입력받기
T = int(input())

# 테스트케이스 숫자 만큼 반복
for tc in range(1, T+1):
    # 숫자 N 입력받기
    N = int(input())
    # 공백있는 text 입력받아서, 리스트로 만들기
    text = list(map(int, input().split()))

    # 일단 ans = 1로 설정
    ans = 1

    # i+1이 N을 벗어나면 안 되기 때문에 N-1까지 범위 설정
    for i in range(N-1):
        # ans = 0 이 되는 조건 설정, 뒤에 값이 앞에 값보다 크거나 같다
        if text[i] <= text[i+1]:
            # if문을 만족하면 ans = 0 으로 설정
            ans = 0
            # if문을 만족하면 for문 종료
            break
    # tc와 ans 출력
    print(f"#{tc} {ans}")
