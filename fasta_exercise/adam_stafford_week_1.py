from Bio import SeqIO
from Bio import pairwise2
from Bio.SeqUtils import GC

data = list(SeqIO.parse("pdm2_neurogenic.fa","fasta")) # Turns sequences into python data structure
seqs = []
for a in data:
    seqs.append(a.seq)
for i in range(0, len(seqs)):
    print("The GC content of seq " + str(i) + " is " + str(GC(seqs[i]))) # Find GC content of sequences
seqaln = pairwise2.align.globalxx(seqs[0], seqs[1]) #Set seqaln to be a pairwise sequence alignment of the first two sequences.
print(seqaln)
