N = 6

# 자식 번호를 인덱스로 부모 번호를 표현하는 트리
# p[x] = y : x번의 부모 번호는 y번
p = [0] * (N + 1)

# 1. 초기화 연산
def make_set(x):
    # 처음에는 자기 자신을 부모로 설정(대표)
    p[x] = x


# for i in range(N+1):
#     # p[i] = i
#     make_set(i)

# 2. 대표 찾는 연산
# x가 속한 집합의 대표를 찾는다.
def find_set(x):
    # x의 부모가 자기 자신을 가리키면 대표
    if p[x] == x :
        return x
    # 아닌 경우는 부모한테 다시 부모를 물어보고.. 대표를 찾을때까지 계속
    else:
        return find_set(p[x])

# 2-2. 경로 압축
# x가 속한 집합의 대표를 찾는 과정에서 만나는 모든 노드의 대표를 업데이트 하여 경로 압축
# 1 ~ N번까지 한번 find_set()을 다 돌리면 모든 원소에 대해 경로압축이 진행된다.
def find_set2(x):
    # x가 집합의 대표가 아니면 경로 압축
    if x != p[x]:
        # 경로 압축
        p[x] = find_set2(x)
    # 집합의 대표라면 바로 return 하면 됨
    else:
        return p[x]



# 3. 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합친다.
# 집합을 합치기 위해서는 반드시 대표를 통해서 진행
def union(x, y):
    # x가 속한 집합의 대표
    king_x = find_set(x)
    # y가 속한 집합의 대표
    king_y = find_set(y)

    # 두 집합을 합친 결과는 하나의 집합이 된다. 대표도 둘중 하나로
    p[king_y] = king_x

for i in range(1,N+1):
    make_set(i)


# 3-2. rank 를 사용한 합치기 연산
# 각 집합을 나타내는 트리의 높이를 rank 라는 이름의 배열에 저장
# 합칠때 두 트리의 랭크를 비교하여 작은 집합을 큰 집합에 합친다.
rank = [0] * (N+1)

def union2(x, y):
    king_x = find_set2(x)
    king_y = find_set2(y)

    # 합칠때 작은 집합을 큰 집합에 합치자.
    # 두 집합의 랭크를 비교해서 더 큰쪽을 대표로 하겠다.
    # 그렇게 하면 큰 집합의 랭크는 변화가 없다.
    if rank[king_x] > rank[king_y]:
        p[king_y] = king_x
    else:
        p[king_x] = king_y

        # 두 집합의 랭크가 같은 경우는 대표를 정하고, 대표쪽 랭크를 + 1
        if rank[king_x] == rank[king_y]:
            # 위에서 대표를 y로 정했으니, y의 랭크를 + 1
            rank[king_y] += 1







# union(1,3)
# union(2,3)
# union(5,6)
#
# print(p)
# print(find_set(6))

for i in range(1,6):
    union(i+1,i)

print(p)