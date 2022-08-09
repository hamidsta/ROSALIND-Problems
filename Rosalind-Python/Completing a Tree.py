
dat = "C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_tree.txt"

with open(dat, "r") as f:
    n = int(f.readline())
    list = [line.strip().split(" ") for line in f]

x = []
nodes = set()
for i, j in list:
    if i in nodes or j in nodes:
        for st in x:
            if i in st or j in st:
                x[x.index(st)].append(i)
                x[x.index(st)].append(j)
                nodes.add(i), nodes.add(j)
    else:
        x.append([i,j])
        nodes.add(i), nodes.add(j)

l = len(x)
for i in range(l):
    for j in range(l):
        if i==j:
           break
        if len(set(x[i] + x[j])) < len(x[i]) + len(x[j]):
            x[i] = list(set(x[i] + x[j]))
            x[j] = []
x = [i for i in x if i]

result = (n -len(nodes)) + len(x) - 1
print(result)