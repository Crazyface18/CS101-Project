"""
this function is supposed to accept a list of DNA strings & return the index
of which string has the highest "GC" content, along with its percentage of
"C" or "G" in the specified string.
"""

def gc_content(dna_list):
    counts = []
    for string in dna_list:
        count_G = string.count("G")
        count_C = string.count("C")
        count = count_C + count_G
        counts.append(count)
    max_count = max(counts) # finds maximum in the list counts
    index = counts.index(max_count)
    percentage = (max_count/len(dna_list[index])) * 100
    return (index, percentage)
