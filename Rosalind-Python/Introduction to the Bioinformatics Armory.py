
def bioinformatics(y):
    x = ["A", "C", "G", "T"]
    counts = {i:y.count(i) for i in x}
    return counts

    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_bioinformatics.txt", "r") as f:
        y = f.readline().strip()
    counts = bioinformatics(y)
    for x,y in counts.items():
        print(v, end=" ")