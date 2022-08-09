def Mrna_inference(y):
    codons = {'F': ['UUU', 'UUC'],
              'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Y': ['UAU', 'UAC'],
              '*': ['Ui', 'UAG', 'UGA'],
              'C': ['UGU', 'UGC'],
              'W': ['UGG'],
              'P': ['CCU', 'CCC', 'CCA', 'CCG'],
              'H': ['CAU', 'CAC'],
              'Q': ['Ci', 'CAG'],
              'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'V': ['GUU', 'GUC', 'GUA', 'GUG'],
              'A': ['GCU', 'GCC', 'GCA', 'GCG'],
              'D': ['GAU', 'GAC'],
              'E': ['Gi', 'GAG'],
              'G': ['GGU', 'GGC', 'GGA', 'GGG'],
              'I': ['AUU', 'AUC', 'AUA'],
              'M': ['AUG'],
              'T': ['ACU', 'ACC', 'ACA', 'ACG'],
              'N': ['iU', 'iC'],
              'K': ['iA', 'iG']}
    x = 1
    for i in y:
        x = x * len(codons[i])
    x = x*len(codons["*"])
    return x % 1000000


with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_Mrna_inference.txt", 'r') as f:
    y = f.readline().strip()
    x = Mrna_inference(y)
    print(x)