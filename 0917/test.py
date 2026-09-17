def pre_order(T):
    if T:
        print(T)
        pre_order(left[T])
        pre_order(right[T])