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
