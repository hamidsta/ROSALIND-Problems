
from Bio import SeqIO

name, string = [], []
with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_pdst.txt", "r") as fasta_file:
	for i in SeqIO.parse(fasta_file, "fasta_filesta"):
		name.append(str(i.name))
		string.append(str(i.seq))

def distance(x, y):
    n = len(x)
    m = 0
    for i in range(n):
        if x[i] != y[i]:
            m += 1
    return '%.5f'% (float(m)/n)

for i in range(len(name)):
    for j in range(len(name)):
        print(distance(string[i],string[j]), end=" ")
    print('')