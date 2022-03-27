def find_splice(dna_motif, dna):
    position_list = []
    counter = 0 #for iterating through dna
    while (counter < len(dna) and dna_motif): #checks through dna_motif & iterates through dna
        if (dna_motif[0] == dna[counter]):
            position_list.append(counter)
            dna_motif = dna_motif[1:] #removes the first letter of motif
        counter += 1
    return position_list
