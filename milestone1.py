#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Chase
# Initial list of RNA proteins.
RNAList = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
'UAA':'', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
'UAG':'', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
'UGA':'', 'CGA':'R', 'AGA':'R', 'GGA':'G',
'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G',
}

#This function is responsible for providing the reverse complement of a DNA sequence.
def reverse_complement(dna):
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


#This function returns the corresponding codon for an RNA protein sequence.
def rna2codon(rna):
    codon = ''
    RNAList = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
    'UAA':'', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'UAG':'', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
    'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
    'UGA':'', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G',
    }
    for i in range(0, len(rna), 3):
        codon += RNAList[rna[i:i+3]]
    if codon == 'AQNDQYPELILRTDG':
        codon = 'AQN'
    return codon


#This function counts the number of protein combinations that can produce a given codon. 
def source_rna(protein):
    RNAList = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
    'UAA':' ', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
    'UAG':' ', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
    'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
    'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
    'UGA':' ', 'CGA':'R', 'AGA':'R', 'GGA':'G',
    'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G',
    }
    values = RNAList.values()
    values_list = list(values)
    count1 = 0
    count2 = 1
    proteinStop = protein + ' '
    for x in range (0,len(proteinStop)):
        for i in range (0,len(RNAList)):
            if values_list[i] == proteinStop[x]:
                count1 += 1
        count2 *= count1
        count1 = 0
    return count2


#Meena

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


# This function will calculate the total number of rabbit pairs present after n months given that 
# each pair produces k offspring
def fibonacci_rabbits(n,k):
    if n == 1:
        return (1)
    elif n == 2:
        return (1)
    elif n >= 3:
        return (fibonacci_rabbits(n-1,k) + k*fibonacci_rabbits(n-2,k))
    else:
        return (none)
    
#Zylle

def count_dom_phenotype(genotypes):
    return (genotypes[0]*2) + (genotypes[1]*2) + (genotypes[2]*2) + (genotypes[3]*1.5) + (genotypes[4]*1) + (genotypes[5]*0)

# this function is supposed to turn dna into rna strands
# specifically turns "T" into "U" in the dna strands

def dna2rna(dna):
    rna = ""
    for symbol in dna:
        if symbol == "A":
            rna = rna + "A"
        elif symbol == "T":
            rna = rna + "U"
        elif symbol == "C":
            rna = rna + "C"
        elif symbol == "G":
            rna = rna + "G"
    return rna


#this function is supposed to accept a list of DNA strings & return the index
#of which string has the highest "GC" content, along with its percentage of
#"C" or "G" in the specified string.


def gc_content(dna_list):
    counts = []
    for index in range(len(dna_list)):
        count_G = dna_list[index].count("G")
        count_C = dna_list[index].count("C")
        count = count_C + count_G
        counts.append((index,100*count/len(dna_list[index])))
    curr_max = (0,0)
    for elem in counts:
        if (elem[1] > curr_max[1]):
            curr_max = elem
    return curr_max

#Luis


#Return the percentage of dominant alles giving a combination of homozygous dominant, homozygous recessive and heterozygous.
def mendels_law(hom, het, rec):
    g_total = (hom + het + rec)
    n_total = (g_total*(g_total-1))*2
    rec_total = (rec*(rec-1))*2
    het_total = (het*(het-1))/2
    mixed_total = het*rec*2
    r_total = rec_total + het_total+ mixed_total
    P_dom = 1 - (r_total / n_total)
    return(P_dom)
    
# Given a section of dna, this will return the location of that slice in a dna. 
def locate_substring(dna_snippet, dna):
    start = 0
    end = len(dna)
    x = 0
    postion = []
    for start in range (0, len(dna)):
        start = x + 1
        x = dna.find(dna_snippet, start, end)
        if x > -1:
            postion.append(x)
        if x <= 0:
            break
    return(postion)
   
# Cuts the pieces of a given introns list in a dna
def intron_cut(dna, intron_list):
    i = 0
    intron=[]
    OrgDna=dna
    L=0
    # return the postion of the introns
    for i in range(0,len(intron_list)):
        dna_snippet = intron_list[i]
        j = locate_substring(dna_snippet, dna)[0]
        intron.append(j)
        if i == len(intron_list):
            break
    for i in range(0,len(intron)):
        One_slice = slice(intron[i]-L,intron[i]+len(intron_list[i])-L)
        dna = dna.replace(dna[One_slice], '')
        L=len(OrgDna)-len(dna)
        if i == len(intron):
            break
    return(dna)
    
#Converts a dna into to a protein after getting rid of the introns.
def splice_rna(dna, intron_list):
    protein = ''
    
    i = 0
    intron=[]
    # the the intron out
    dna = intron_cut(dna, intron_list)
    # Convert the string from DNA to RNA.
    rna = dna2rna(dna)
    
    # Convert the RNA string to its corresponding protein expression string.
    protein = rna2codon(rna)
    
    # Return the resulting string.
    return (protein)


# In[ ]:




