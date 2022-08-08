
from Bio import Entrez
from bs4 import BeautifulSoup

def get_nucleo_genbank(genus_name, date1, date2):
    Entrez.email = "***@******"
    term = '"{}"[Organism] AND ("{}"[Publication Date] : "{}"[Publication Date])'.format(genus_name, date1, date2)
    handle = Entrez.esearch(db="nucleotide", term=term)
    records = handle.read()
    soup = BeautifulSoup(records,'html.parser')
    handle.close()
    return soup.count.text


if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_gbk.txt", "r") as f:
        genus_name = f.readline().strip()
        date1 = f.readline().strip()
        date2 = f.readline().strip()
    count = get_nucleo_genbank(genus_name, date1, date2)
    print(count)