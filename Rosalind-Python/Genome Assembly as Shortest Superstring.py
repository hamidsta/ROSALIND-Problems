from Bio import SeqIO


def stings_overlap(x, y):
    merge_x = []
    overlaping = []
    for i in range(len(x)):
        if x[i:] == y[:len(x) - i]:
            overlaping.append(x[i:])
            merge_x.append(x + y[len(x) - i:])
            break
    for i in range(len(y)):
        if y[i:] == x[:len(y) - i]:
            overlaping.append(y[i:])
            merge_x.append(y + x[len(y) - i:])
            break
    if not overlaping:
        return "", ""

    x_combined = min(merge_x, key=len)
    x_overlaped = max(overlaping, key=len)
    return x_combined, x_overlaped


def shortest_superstring(x):
    temporary = x

    while len(temporary) > 1:
        overlaping_string = ""
        overlaping_string_pair = []
        overlaping_string_length = 0

        for i in range(len(temporary) - 1):
            for j in range(i + 1, len(temporary)):
                x_combined, x_overlaped = stings_overlap(temporary[i], temporary[j])
                if len(x_overlaped) > overlaping_string_length:
                    overlaping_string = x_combined
                    overlaping_string_pair = [temporary[i], temporary[j]]
                    overlaping_string_length = len(x_overlaped)

        temporary.remove(overlaping_string_pair[0])
        temporary.remove(overlaping_string_pair[1])
        temporary.append(overlaping_string)

    return temporary


    name, string = [], []
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_long.txt", 'r') as fa:
        for i in SeqIO.parse(fa, 'fasta'):
            name.append(str(i.name))
            string.append(str(i.seq))
    shortest_superstring = shortest_superstring(string)
    print(shortest_superstring)