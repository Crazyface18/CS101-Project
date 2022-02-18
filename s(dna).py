#!/usr/bin/env python
# coding: utf-8

# In[40]:


# s(dna) function 
def dnac(dna):
    dna ='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    countA = dna.count('A')
    countC = dna.count('C')
    countG = dna.count('G')
    countT = dna.count('T')
    dnac = {
        'A': countA,
        'C': countC, 
        'G': countG, 
        'T': countT
    }
    return(dnac)
print(dnac(dna))


# In[19]:





# In[ ]:




