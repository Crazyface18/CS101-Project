#!/usr/bin/env python
# coding: utf-8

# In[44]:


# s(dna) function 
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





# In[ ]:




