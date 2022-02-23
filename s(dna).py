#!/usr/bin/env python
# coding: utf-8

# In[57]:


# s(dna) function
# The purpose of this function is to count the number of nucleotides in a given strand and return a dictionary showing the counts for each nucleotide. 
dna =''
def s(dna):
    countA = dna.count('A')
    countC = dna.count('C')
    countG = dna.count('G')
    countT = dna.count('T')
    s = {
        'A': countA,
        'C': countC, 
        'G': countG, 
        'T': countT
    }
    return(s)
