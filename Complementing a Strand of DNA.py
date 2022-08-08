def DNAstrand(string):
    strand = ""
    for i in string[::-1]:
        if i == "A":
            strand += "T"
        if i == "T":
            strand += "A"
        if i == "C":
            strand += "G"
        if i == "G":
            strand += "C"
    return strand


if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_revc.txt", "r") as f:
        string = f.readline().strip()
        strand = DNAstrand(string)
        print(strand)