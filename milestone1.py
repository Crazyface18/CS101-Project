#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
# hamming_dist
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
# fibonacci_rabbits(n,k)
# This function calculates the total number of rabbit pairs that will be present after n months, given that every rabbit
# pair produces k rabbit pairs in their next litter of next month
def fibonacci_rabbits(n,k):
    if n == 0:
        return (0)
    elif n == 1:
        return (1)
    elif n == 2:
        return (1)
    elif n > 2:
        return (fibonacci_rabbits(n-1,k) + k*fibonacci_rabbits(n-2,k))
    else:
        return (none)


# In[ ]:




