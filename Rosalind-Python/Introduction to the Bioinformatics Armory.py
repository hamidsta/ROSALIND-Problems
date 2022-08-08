
def ini(dna):
    symbols = ["A", "C", "G", "T"]
    symbols_count = {i:dna.count(i) for i in symbols}
    return symbols_count

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_ini.txt", "r") as f:
        dna = f.readline().strip()
    symbols_count = ini(dna)
    for k,v in symbols_count.items():
        print(v, end=" ")