def postorder(T):
    if T == 0:
        return 0
    l = postorder(left[T])
    r = postorder(right[T])
    return l + r + 1

# def preorder(t):
#     global count
#     if t:
#         # t번 노드에 도착 할때마다 노드 개수 +1
#         count += 1
#         preorder(left[t])
#         preorder(right[t])




T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선의 개수 E, 서브트리의 루트 N
    tree = list(map(int, input().split()))  # 트리의 정보

    # 부모 노드 번호를 인덱스로 사용하는 방법
    # 자식 노드 빈리스트 만들기
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    # 입력받은 트리 정보를 간선의 개수만큼 자른다
    for i in range(E):
        p = tree[i*2]       # 부모노드번호(앞)
        c = tree[i*2+1]     # 자식노드번호(뒤)

        # 왼쪽 자식과 오른쪽 자식 분리
        # 왼쪽 자식이 비어있으면 왼쪽에 넣고, 아니면 오른쪽에 넣는다
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    # 노드 N을 루트로 하는 서브트리의 노드 개수 구하기
    cnt = postorder(N)
    print(f'#{tc} {cnt}')

