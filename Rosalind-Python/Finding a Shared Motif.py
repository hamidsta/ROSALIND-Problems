from Bio import SeqIO


def short(x):
    min_len = 10000
    short = ''
    for i in x.keys():
        if len(x[i]) < min_len:
            min_len = len(x[i])
            short = x[i]
    return short


def shared_motif(seq):
    seq = short(seq)
    motif = set()
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            motif.add(seq[i:j])
    for x in seq.values():
        update_motif = list(motif)
        for w in update_motif:
            if w not in x:
                motif.remove(w)
    n = 0
    motif_long = ''
    for i in motif:
        if len(i) > n:
            motif_long = i
            n = len(i)
    return motif_long


    seq_name, seq_string = [], []
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_lcsm.txt", 'r') as fa:
        for seq_record in SeqIO.parse(fa, 'fasta'):
            seq_name.append(str(seq_record.name))
            seq_string.append(str(seq_record.seq))
    seq = {seq_name[i]: seq_string[i] for i in range(len(seq_name))}
    print(shared_motif(seq))


