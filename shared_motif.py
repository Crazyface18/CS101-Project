#!/usr/bin/env python
# coding: utf-8

# In[134]:


def shared_motif(dna_list): 
    substring = '' #Defines the substring variable
    for i in range(len(dna_list[0])): 
        for x in range((len(dna_list[0])+1)-i):
            for y in range(len(dna_list)): #For loops are used to set up the iterations through all of the possible combinations of dna values
                if dna_list[0][i:i+x] not in dna_list[y]: #If function used to verify that the value it is currently checking has a corresponding value in the next string
                    compare = False
                    break
                compare = True
            if x > len(substring) and compare:#If the substring it has located is longer than the previously recorded substring, and is present in the next string in the list, it saves the new substring
                substring = dna_list[0][i:i+x]
    return substring
