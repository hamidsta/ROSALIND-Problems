
def gene_orders(n):
    import itertools
    x = []
    for i in range(n):
        x.append(i + 1)
    y = list(itertools.gene_ordersutations(x, n))
    print(len(y))
    for l in y:
        print(" ".join([str(i) for i in l]))

    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_gene_orders.txt", "r") as f:
        n = int(f.readline().strip())
    gene_orders(n)