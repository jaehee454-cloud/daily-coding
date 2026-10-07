"""
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""

V, E = map(int, input().split())

# 인접 리스트
# G[a] = [(b,2), (c,4)]
# => 정점 a에서 b로 가는 간선의 가중치2, a에서 c로 가는 간선의 가중치4
G = [[] for _ in range(V)]

for i in range(E):
    # s,e,w (s에서 e로가는 간선의 가중치는 w)
    s, e, w = map(int, input().split())
    G[s].append((e, w))

# 가중치가 최소인 간선을 선택시 힙을 사용하여 최적화
from heapq import heappop, heappush

# D: 최단 거리를 저장할 리스트
# D[i] : 시작정점에서 i정점까지 최단 거리(가중치 합)
INF = 1e9
D = [INF] * V

# s : 시작 정점 번호
# s에서 시작해서 다른 모든 정점까지의 최단거리를 구하는게 목표
def dijkstra(s):
    # 가중치가 가장 작은 간선을 선택할때 효율적으로 선택
    heap = []

    # 시작정점을 처리 (s-s까지 가는데 가중치를 0, s)
    heappush(heap, (0, s))
    # 시작정점까지의 최단거리는 0으로 두고 시작
    D[s] = 0

    # 힙에 간선 정보가 남아있으면 계속
    while heap:

        # 다음에 도착가능한 정점 중에 최단거리(가중치가 최소)인 정점을 선택한다
        # 다음 도착 정점 v, 그때 간선의 가중치가 w
        w, v = heappop(heap)

        # 내가 예전에 v를 선택한적이 있는가? 원래 방문배열을 써야 하지만
        # 힙의 특성을 생각하면.. 힙 안에는 v까지 도착하는 가중치가 여러개 있을꺼고, 가장 먼저 꺼내는 것은 그중에 최소 일 것이다.
        # 최소거리는 이미 D[v]에 저장을 한 상태고, 새로 꺼낸 거리가 D[v] 보다 크면 또 계산할 필요가 없다.
        if w > D[v]:
            continue

        # v를 거쳐서 갈 수 있는 새로운 경로들이 생겼다
        # 이 새로운 경로가 최단 거리가 되는지 확인하고 갱신
        # v와 인접한 정점들을 모두 확인하고, 최단경로라면 갱신
        for nv, nw in G[v]:
            # v와 인접한 정점 nv, 그때 가중치 nw
            # s에서 시작해서 v를 거쳐 nv로 가는 이 새로운길이 최단경로인가??
            # s에서 nv까지의 최단거리 = s에서 v까지의 최단거리 + v-nv 거리
            # 이 거리가 이전에 계산한 최단거리보다 작은가?
            new_distance = w + nw

            if new_distance < D[nv]:
                D[nv] = new_distance
                # 힙에 최단거리를 사용해서 nv까지 도착한 정보를 추가
                heappush(heap, (new_distance, nv))

dijkstra(0)

print(D)