
from Bio import Entrez
from bs4 import BeautifulSoup

def genbank(genus_name, date1, date2):
    mail = "***@******"
    term = '"{}"[Organism] AND ("{}"[Publication Date] : "{}"[Publication Date])'.format(genus_name, date1, date2)
    handle = Entrez.esearch(db="nucleotide", term=term)
    records = handle.read()
    soup = BeautifulSoup(records,'html.parser')
    handle.close()
    return soup.count.text


    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_gbk.txt", "r") as f:
        genus_name = f.readline().strip()
        date1 = f.readline().strip()
        date2 = f.readline().strip()
    count = genbank(genus_name, date1, date2)
    print(count)