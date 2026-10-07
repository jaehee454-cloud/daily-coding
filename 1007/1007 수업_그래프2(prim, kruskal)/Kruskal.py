"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""

V, E = map(int, input().split())

# 간선 정보를 저장할 리스트
edges = []

for i in range(E):
    # s와 e를 잇는 간선 가중치 w
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

# 입력 받을때 가중치를 2번 인덱스에 넣었으니 2번 인덱스 원소 기준으로 정렬
edges.sort(key=lambda x: x[2])

# 크루스칼 알고리즘은 사이클의 유무를 상호배타집합을 통해 확인한다.

# make-set
p = [i for i in range(V)]

# find-set
def find_set(x):
    if x == p[x]:
        return x

    # 경로 압축
    p[x] = find_set(p[x])
    return p[x]

# union
def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    p[king_y] = king_x

# 선택한 간선의 개수가 V-1
cnt = 0

# 최소 가중치 합
MIN = 0

# 정렬이 되어있는 리스트에서 간선 하나씩 꺼내서 확인
# 싸이클이 생기면 건너뛰고 다음 간선확인, 간선 V-1개 모았으면 종료
for s, e, w in edges:

    # 정점 s와 e가 속한 집합의 대표를 찾아서 비교
    # 대표가 다르다 => 다른 집합에 속해있다 => 이어도 싸이클이 생기지 않는다
    if find_set(s) != find_set(e):
        union(s,e)
        cnt += 1
        MIN += w

        if cnt == V-1:
            break

print(f"MST 최소 가중치 합 : {MIN}")
