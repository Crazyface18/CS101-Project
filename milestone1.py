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
            rna = rna + "G"
        elif symbol == "G":
            rna = rna + "C"
    return rna

"""
this function is supposed to take 6 nonnegative integers, which corresponds to
a number of couples in a population

each couple makes two offspring. this function will return how many offspring
are created with the dominant phenotype.
"""

def count_dom_phenotype(genotypes):
    return (genotypes[0]*2) + (genotypes[1]*2) + (genotypes[2]*2) + (genotypes[3]*1.5) + (genotypes[4]*1) + (genotypes[5]*0)

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

