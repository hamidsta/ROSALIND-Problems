def mendel(x, y, z):
    i = y * y + 4 * z * z + 4 * y * z - 4 * z - y
    j = 4 * (x + y + z) * (x + y + n - 1)
    rst = 1 - float(i) / j
    return rst


if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_iprb.txt", 'r') as f:
        x, y, z = map(int, f.readline().strip().split(" "))
        print(mendel(x, y, z))