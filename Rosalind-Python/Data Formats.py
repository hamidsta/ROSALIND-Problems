
from Bio import Entrez, SeqIO

def short_entry(entry_ids):
    Entrez.email = "***@*****"
    handle = Entrez.efetch(db="nucleotide", id=[", ".join(entry_ids)], rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    print(min(records, key=lambda s: len(s.seq)).format("fasta"))

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_frmt.txt", "r") as f:
        entry_ids = f.readline().strip().split()
    short_entry(entry_ids)