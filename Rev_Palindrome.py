#!/usr/bin/env python
# coding: utf-8

# In[18]:


def rev_palindrome(dna):
    tuples = []
    def reverse_compliment(dna):#reverse compliment function from Milestone 1
        reverse = ''
        for i in range(0,len(dna)):
            if dna[i] == 'A':
                reverse += 'T'
            elif dna[i] == 'T':
                reverse += 'A'
            elif dna[i] == 'C':
                reverse += 'G'
            elif dna[i] == 'G':
                reverse += 'C'
        return reverse[::-1]
    
    
    for x in range(len(dna)):#this sets the initial value that the iteration will start at
        for y in range(4,13):#this counts up over the possible lengths of the palindromes
            if y > (len(dna)-x):#this is a safety stop which will automatically stop the funtion if it is about to exceed the length of the string.
                break
            elif reverse_compliment(dna[x:x+y]) == dna[x:x+y]:#this checks the currently selected substring against it's equivalent reverse complement. If they are equal, it saves the position and length.
                tuples.append(tuple([x,y]))
    return (tuples)
