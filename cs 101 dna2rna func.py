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
