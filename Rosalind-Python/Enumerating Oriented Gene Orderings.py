
from Bio import SeqIO
import itertools

def oriented_genes(n):
    x = []
    for i in range(n):
        x.extend([i + 1, - i - 1])
    y = list(itertools.permutations(x, n))

    z = []
    for a in y:
        aset = set()
        for i in a:
            aset.add(abs(i))
        if len(aset) < len(a):
            z.append(a)

    w = list(set(y) ^ set(z))
    print(len(w))
    for i in w:
        a = str(i)
        a = a.replace('(', '').replace(',', '').replace(')', '')
        print(a)

    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_sign.txt", "r") as f:
        n = int(f.readline().strip())
        oriented_genes(n)