"""week_1.py: Some very basic data manipulation with pdm2_neurogenic.fa using BioPython."""

__author__ = "Tianhao Zhang"

from Bio import SeqIO
from Bio import pairwise2
from Bio.SeqUtils import GC


# Reads in the pdm2_neurogenic.fa file and turn it into a python list
record_list = list(SeqIO.parse("pdm2_neurogenic.fa", "fasta"))

# Reads in the pdm2_neurogenic.fa file and turn it into a python dictionary
record_dict = SeqIO.to_dict(SeqIO.parse("pdm2_neurogenic.fa", "fasta"))

# Code used for visually examining the above list and dictionary
# for i in record_list:
# 	print(i.seq)
# for i in record_dict:
# 	print(i) 


# Makes an alignment for the first two sequences, match scroe 1, dismatch score 0, no gap penalty
alignments01 = pairwise2.align.globalxx(record_list[0].seq, record_list[1].seq)

# Makes an alignment for the third and the fourth sequences.
# Identical characters are given 2 points, 1 point is deducted for each non-identical character.
# 0.5 points are deducted when opening a gap, and 0.1 points are deducted when extending it.
alignments23 = pairwise2.align.globalms(record_list[2].seq, record_list[3].seq, 2, -1, -.5, -.1)

# Code used for visually examining the above two alignments
# print("length of alignments01 is " + str(len(alignments01)))
# for a in alignments01[0]:
# 	print (a)
# print("length of alignments23 is " + str(len(alignments23)))
# for a in alignments23[0]:
# 	print (a)


# Measures GC content per sequence, stores in the result in a list
GC_list = list(map(GC, [i.seq for i in record_list]))
print(GC_list)
# Measures GC content per sequence, stores in the result in a dictionary
# Maps sequence id to GC cpercentage.
# Rounded to 2 digits precision.
GC_dict = dict(map(lambda x : (x[0], round(GC(x[1].seq), 2))
					 ,record_dict.items()))
print(GC_dict)



