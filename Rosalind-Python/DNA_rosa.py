"""
take A DNA string  of length at most 1000 nt
Return number of nucleotide occurence
"""

def count_dna(string):
    countA = string.count("A")
    countG = string.count("G")
    countT = string.count("T")
    countC= string.count("C")

    return countA, countC, countG, countT

print(countA, countC, countG, countT)

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_dna.txt", 'r') as f:
        string = f.readline().strip()
        countA, countC, countG, countT = count_dna(string)
        print(countA, countC, countG, countT)