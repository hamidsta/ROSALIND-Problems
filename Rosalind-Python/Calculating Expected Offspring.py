def off_spring(x):
    offspring = (1*x[0] + 1*x[1] + 1*x[2] + 0.75*x[3] + 0.5*x[4] + 0*x[5]) * 2
    return offspring

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_iev.txt", "r") as f:
        l = [float(i) for i in f.readline().strip().split(" ")]
    print(off_spring(l))