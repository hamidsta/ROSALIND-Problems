
from Bio import SeqIO

def catalan_numbers(s, nœuds, memo):
    x = int(nœuds/2)
    if x <= 1:
        return 1
    if memo.get((s, nœuds),0):
        return memo[(s, nœuds)]
    Cn = 0
    for k in range(1, 2*x, 2):
        a, u, c, g = s[1:k].count("A"), s[1:k].count("U"), s[1:k].count("C"), s[1:k].count("G")
        if a==u and c==g and (s[0], s[k]) in [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")]:
            Cn += catalan_numbers(s[1:k], k-1, memo) * catalan_numbers(s[k+1:], 2*x-k-1, memo)
    memo[(s, nœuds)] = Cn
    return Cn


    seq_name, seq_string = [], []
    with open ("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_cat.txt",'r') as fa:
        for seq_record in SeqIO.parse(fa,'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))

    s = seq_string[0]
    print(s)
    nodes = len(s)
    catalan_memo = {}
    catalan_number= catalan_numbers(s, nodes, catalan_memo)
    print("catalan number: {}".format(catalan_number))
    print("modulo 1,000,000: {}".format(catalan_number%1000000))