"""
this function is supposed to accept a list of DNA strings & return the index
of which string has the highest "GC" content, along with its percentage of
"C" or "G" in the specified string.
"""

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
