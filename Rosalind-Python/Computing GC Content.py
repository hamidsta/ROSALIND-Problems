
from Bio import SeqIO

def gc_percent_percent(strings):
    gc_contents = {}
    for k, v in strings.items():
        gc_content = (v.count("G") + v.count("C")) / len(v)
        gc_contents[k] = gc_content
    gc_contents = sorted(gc_contents.items(), key=lambda d: d[1], reverse = True)
    high = gc_contents[0]
    return high

    name, string = [], []
    with open ("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_gc_percent.txt",'r') as fa:
        for seq_record  in SeqIO.parse(fa,'fasta'):
            name.append(str(seq_record.name))
            string.append(str(seq_record.seq))
    strings = {name[i]:string[i] for i in range(len(name))}
    high = gc_percent(strings)
    print(high[0])
    print(high[1]*100)