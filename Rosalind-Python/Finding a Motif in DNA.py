
x ="GATATATGCATATACTT"
y="ATAT"

def motif_sub(string1, string2):
    loc = []
    for i in range(len(string1)):
        if string2 == string1[i: i+len(string2)]:
            loc.append(i+1)
    return loc






if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_subs.txt", 'r') as f:
        string1 = f.readline().strip()
        string2 = f.readline().strip()
    loc = motif_sub(string1, string2)
    for i in loc:
        print(i, end=" ")