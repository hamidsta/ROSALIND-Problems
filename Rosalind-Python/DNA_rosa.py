

def DNA(x):
    Nucleotide_A = x.count("A")
    Nucleotide_G = x.count("G")
    Nucleotide_T = x.count("T")
    Nucleotide_C= x.count("C")

    return Nucleotide_A, Nucleotide_C, Nucleotide_G, Nucleotide_T

print(Nucleotide_A, Nucleotide_C, Nucleotide_G, Nucleotide_T)

with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_dna.txt", 'r') as f:
    x = f.readline().strip()
    Nucleotide_A, Nucleotide_C, Nucleotide_G, Nucleotide_T = DNA(x)
    print(Nucleotide_A, Nucleotide_C, Nucleotide_G, Nucleotide_T)