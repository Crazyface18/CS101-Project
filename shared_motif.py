#!/usr/bin/env python
# coding: utf-8

# In[134]:


def shared_motif(dna_list):
    substring = ''
    for i in range(len(dna_list[0])):
        for x in range((len(dna_list[0])+1)-i):
            for y in range(len(dna_list)):
                if dna_list[0][i:i+x] not in dna_list[y]:
                    compare = False
                    break
                compare = True
            if x > len(substring) and compare:
                substring = dna_list[0][i:i+x]
    return substring
print (shared_motif(["ATATACAAAA", "ATACAGABBB", "GGTATACAAAAAAAAAAAA"]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




