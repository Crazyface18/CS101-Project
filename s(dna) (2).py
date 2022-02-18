#!/usr/bin/env python
# coding: utf-8

# In[44]:


# s(dna) function
# The purposeo of this function is to count the number of nucleotides in a given strand and return a dictionary showing the counts for each nucleotide. 
def s(dna):
    dna =''
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
print(s(dna))


# In[45]:


#Test function 
def s(dna):
    dna ='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
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
print(s(dna))


# In[ ]:




