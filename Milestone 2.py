#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Chase 
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


#Luis
def get_edges(dna_dict):
    NameAndDna = list(dna_dict.items())
    ListOfItems = []
    Adjacent_List = []
    
    for item in range(0,len(NameAndDna)):
        find = NameAndDna[item]
        Key = find[0]
        ListOfItems.append(Key)
        Key = find[1]
        ListOfItems.append(Key)
    
# Runs the loop to check the back three charaters to the first three of the piece of Dna after it
#It goes from front to back of the ListofItems

    for item in range(1,len(ListOfItems)-2,2):
        for shift in range(2,len(ListOfItems)-(item+1)+2,2):
            #print(j, 'Bye')
            One = ListOfItems[item]
            Two = ListOfItems[item + shift]
            if One[-3:len(One)] == Two[0:3]:
                Adjacent_Pair = ListOfItems[item - 1],ListOfItems[item + shift -1]
                Adjacent_List.append(Adjacent_Pair)
                
# Runs the loop to check the back three charaters to the first three of the piece of Dna before it.
#It goes from back to front of the ListofItems

    for item in range(1,len(ListOfItems)-2,2):
        item = len(ListOfItems) - item
        for shift in range(2,len(ListOfItems)-(item+1)+2,2):
            One = ListOfItems[item]
            Two = ListOfItems[item - shift]
            if One[-3:len(One)] == Two[0:3]:
                Adjacent_Pair = ListOfItems[item-1],ListOfItems[item- shift -1]
                Adjacent_List.append(Adjacent_Pair)
                
    return(Adjacent_List)
    
    # -----------

import math
def random_genome(dna, gc_content):
    GC_Count = [] # A list of the times that G and C in the dna 
    
    # A loop to find how many G and C in dna
    for letter in dna: 
        if letter == 'C':
            GC_Count.append(1)
        if letter == 'G':
            GC_Count.append(1)
    # Stores amount of GC and AT count respectfully 
    GC_Amount = sum(GC_Count)
    AT_Amount = len(dna) - GC_Amount
    Log_Pro = []
    # Looks through the gc-content and find the log probabilities then places that into the list Log_Pro
    for value in gc_content:
        Pro_Same = math.log10(((value/2)**GC_Amount) * (((1-value)/2)**AT_Amount))
        Log_Pro.append(Pro_Same)
    return(Log_Pro)


#Zylle
def find_splice(dna_motif, dna):
    position_list = []
    index = 0 #iterates through dna
    while dna_motif: 
        if (index >= len(dna)):
            return [] #returns empty list if sequence not found
        if (dna_motif[0] == dna[index]):
            position_list.append(index)
            dna_motif = dna_motif[1:] #removes the found letter of motif
        index += 1
    return position_list


def assemble_genome(dna_list):
    while len(dna_list) > 1: #loops until one value is left
        temp = ""
        max_first = 0
        max_second = 1
        max_overlap = overlap_length(dna_list[0],dna_list[1]) #sets default max case for comparison

        for i in range(0,len(dna_list)): #iterates through all possible comparisons
            for j in range(0,len(dna_list)):
                if (i==j): #ignore comparisons with themselves
                    continue
                if (i==0) and (j==1): #default case, we can ignore it also
                    continue
                else: #real comparisons
                    if (overlap_length(dna_list[i],dna_list[j]) > max_overlap): #tests current overlap with previous max overlap
                        max_first = i
                        max_second = j
                        max_overlap = overlap_length(dna_list[i],dna_list[j]) #set newest set to current max
                    elif (overlap_length(dna_list[i],dna_list[j]) == max_overlap) and (dna_list[i] < dna_list[max_first]):
                        max_first = i
                        max_second = j
                        max_overlap = overlap_length(dna_list[i],dna_list[j])

        if (max_overlap == 0):
            dna_list[max_first] = dna_list[max_first] + dna_list[max_second]
        else:
            dna_list[max_first] = dna_list[max_first][:0-max_overlap] + dna_list[max_second] #combine and replace
        dna_list.pop(max_second)

    return dna_list[0] #once loop is done, return only string left in the list

def overlap_length(str1, str2):
    overlap = 0
    for i in range(1,min(len(str1),len(str2))+1): #checks each segment to see if overlap works
        if str1[0-i:] == str2[:i]: #check overlap segment
            overlap = i #set max overlap
    return overlap #return max value


# In[ ]:




