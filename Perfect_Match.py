#!/usr/bin/env python
# coding: utf-8

# In[28]:


def perfect_match(rna):
    GC=0
    AU=0
    from math import factorial
    for i in rna:
        if i == 'G':
            GC+=1
        elif i == 'A':
            AU+=1
    matches = factorial(GC)*factorial(AU)
    return (matches)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




