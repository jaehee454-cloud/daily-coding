T = int(input())

for tc in range(1, T+1):
    txt = list(input())
    cnt = 0
    current = '0'
    for i in range(len(txt)):
        if txt[i] != current:
            cnt += 1
            current = txt[i]

    print(f"#{tc} {cnt}")