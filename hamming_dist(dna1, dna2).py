#!/usr/bin/env python
# coding: utf-8

# In[105]:


# This function will return the hamming distance between 2 strands of nucleotides
dna1 = ""
dna2 = ""
def hamming_dist(dna1,dna2):
    count = 0
    x = len(dna1)
    for nucleotide in range(0,x):
        if dna1[nucleotide] != dna2[nucleotide]:
            count += 1
    return count
