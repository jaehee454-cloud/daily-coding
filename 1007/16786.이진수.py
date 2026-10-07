T = int(input())

for tc in range(1, T+1):
    N, txt = input().split()
    N = int(N)

    stack = []
    K = ""
    for x in txt:
        if x in "ABCDEF":
            if x == "A":
                num = 10
            elif x == "B":
                num = 11
            elif x == "C":
                num = 12
            elif x == "D":
                num = 13
            elif x == "E":
                num = 14
            elif x == "F":
                num = 15
        else:
            num = int(x)
        for _ in range(4):
            stack.append(num%2)
            num = num//2
        for _ in range(4):
            K += str(stack.pop())

    print(f"#{tc} {K}")



# num = 10
# stack = []
# K = ""
# for _ in range(4):
#     stack.append(num%2)
#     num = num//2
# for _ in range(4):
#     K += str(stack.pop())
#
# print(K)