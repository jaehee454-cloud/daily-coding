T = int(input())

for tc in range(1, T+1):
    # V : 노드번호, E : 간선의 개수
    V, E = map(int, input().split())

    edges = []

    for i in range(E):
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    edges.sort(key=lambda x:x[2])

    # 노드 번호가 0~V까지 이므로 range(V+1)
    p = [i for i in range(V+1)]

    # find_set
    def find_set(x):
        if x == p[x]:
            return x

        p[x] = find_set(p[x])
        return p[x]

    # union
    def union(x, y):
        king_x = find_set(x)
        king_y = find_set(y)

        p[king_y] = king_x

    cnt = 0
    MIN = 0

    for s, e, w in edges:
        if find_set(s) != find_set(e):
            union(s, e)
            cnt += 1
            MIN += w

            # 노드번호가 0~V까지 이므로 cnt == V이면 종료
            if cnt == V:
                break

    print(f"#{tc} {MIN}")