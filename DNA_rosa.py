"""
Counting DNA Nucleotides
url: http://rosalind.info/problems/dna/
Given: A DNA string  of length at most 1000 nt
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in
"""

def DNA_COUNT(string):
    countA = string.count("A")
    countG = string.count("G")
    countT = string.count("T")
    countC= string.count("C")

    return countA, countC, countG, countT

print(countA, countC, countG, countT)

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_dna.txt", 'r') as f:
        string = f.readline().strip()
        countA, countC, countG, countT = DNA_COUNT(string)
        print(countA, countC, countG, countT)