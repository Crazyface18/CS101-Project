#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[ ]:




