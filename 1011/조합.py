arr = [1, 2, 3, 4, 5]
N = 5
R = 3
path = []

def comb(start):
    if len(path) == 3:
        print(path)
        return

    for i in range(start, N):
        path.append(arr[i])
        comb(i+1)
        path.pop()

comb(0)