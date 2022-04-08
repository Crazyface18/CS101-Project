#!/usr/bin/env python
# coding: utf-8

# In[28]:


def perfect_match(rna): 
    GC=0
    AU=0 #defining the varriables that will be used.
    from math import factorial #Total number of pairs that is present in a list can be found with the factorial of 1/2 the total number of nodes, so it is imported here.
    for i in rna: #Because there are 2 sets of values that pair together, GC and AU, we basically have two different numbers of pairs. This for loop separates those two sets of pairs.
        if i == 'G': #also, as the total perfect pairs is the factorial of 1/2 the total number of nodes, we only need to count one of the two pairing values. 
            GC+=1
        elif i == 'A':
            AU+=1
    matches = factorial(GC)*factorial(AU) #here we multiply the two sets of perfect pairs together, giving us the total number of perfect pairs.
    return (matches)
