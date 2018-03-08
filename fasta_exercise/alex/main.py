
# coding: utf-8

# # Week 1 FASTA Exercise
# 
# Author: Alex Nakagawa
# 
# Last Updated: March 5, 2018
# 
# <a src='http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc3'>BioPython Tutorial</a>
# 
# <a src='http://biopython.org/DIST/docs/api/'>BioPython Docs</a>

# In[1]:


from __future__ import print_function

from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio import pairwise2

import numpy as np
import pandas as pd

def main():

	# Reading File
	file_name = '../pdm2_neurogenic.fa'

	print("Reading in Original Sequences:")
	sequences = []
	print("Completed Sequences by ID:\n")
	for seq_record in SeqIO.parse(file_name,'fasta'):
	    print(seq_record.id, "\n")
	    sequences.append(seq_record)
	print("Completed.")


	# Turn sequences into a basic Python data structure
	# 
	# `df_sequences`: Pandas Dataframe with one sequence object per row
	# 	`id`: Description header of each sequence
	# 	`seq`: Letter sequence
	# 	`length`: integer length of the sequence
	# 	`func`: 0 for negative function, 1 for positive function
	# 	`GC_ratio`: Ratio of GC pairs to full sequence

	# In[6]:


	df_sequences = pd.DataFrame({"id": [i.id for i in sequences],
	                             "seq": [j.seq for j in sequences],
	                             "length": [len(k.seq) for k in sequences],
	                            })
	df_sequences['func'] = df_sequences['id'].str[-1].replace({'-': 0, '+': 1})
	df_sequences


	# In[39]:


	df_sequences['species'] = df_sequences['id'].str.findall('MEMB(....)')
	df_sequences


	# ### Measure GC content per sequence

	# In[20]:


	df_sequences["GC_ratio"] = df_sequences.seq.apply(GC) / 100.0
	df_sequences


	# ### Alignment Sequence
	# 
	# `pairwise2.align.globalxx`: Pairwise alignment with no cost value for misaligned pairs, and a value of 1 for matched pairs between the two sequences.
	# 
	# `pairwise2.format_alignment(*alignment[0])`: Show matches from start to finish positions as defined by previous function.

	# In[32]:


	alignment_0_1 = pairwise2.align.globalxx(df_sequences.seq.iloc[0], df_sequences.seq.iloc[1])
	print(pairwise2.format_alignment(*alignment_0_1[0]))

