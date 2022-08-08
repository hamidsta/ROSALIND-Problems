def num_rabbits(n, m):
    # n is the n-th month.
    # m is that a rabbit live for m month.
    # in the first month, the num of rabbit is 1.
    num_list = []
    num_list.append(0)
    num_list.append(1)
    for i in range(1, n+1, 1):
        if i < m:
            num_list.append(num_list[i] + num_list[i-1])
        if i == m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
        if i > m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])

    return num_list[n]

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_fibd.txt", "r") as f:
        n, m = map(int, f.readline().strip().split(" "))
    print(num_rabbits(n, m))