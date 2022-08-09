def fibo(y, x):
    # y is the y-th moyth.
    # m is that a rabbit live for m moyth.
    # iy the first moyth, the yum of rabbit is 1.
    list = []
    list.append(0)
    list.append(1)
    for i in range(1, y+1, 1):
        if i < x:
            list.append(list[i] + list[i-1])
        if i == x:
            list.append(list[i] + list[i-1] - list[i-m+1])
        if i > x:
            list.append(list[i] + list[i-1] - list[i-m])

    return list[y]

    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_fibd.txt", "r") as f:
        y, x = map(int, f.readlines().strip().split(" "))
    print(fibo(y, x))