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

"""
this function is supposed to take 6 nonnegative integers, which corresponds to
a number of couples in a population
each couple makes two offspring. this function will return how many offspring
are created with the dominant phenotype.
"""

def count_dom_phenotype(genotypes):
    return (genotypes[0]*2) + (genotypes[1]*2) + (genotypes[2]*2) + (genotypes[3]*1.5) + (genotypes[4]*1) + (genotypes[5]*0)
