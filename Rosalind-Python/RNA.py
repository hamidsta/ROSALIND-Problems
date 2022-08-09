def dna2rna(string):
    return string.replace('T','U')

    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_rna.txt", 'r') as f:
        string = f.readline().strip()
        rst = dna2rna(string)
        print(rst)