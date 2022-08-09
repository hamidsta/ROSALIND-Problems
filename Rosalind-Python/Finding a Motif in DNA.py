

def find_motif(x, y):
    z = []
    for i in range(len(x)):
        if y == x[i: i+len(y)]:
            z.append(i+1)
    return z






    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_subs.txt", 'r') as f:
        x = f.readline().strip()
        y = f.readline().strip()
    z = find_motif(x, y)
    for i in z:
        print(i, end=" ")