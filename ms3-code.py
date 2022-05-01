def load_file(filename):
    txt_file = open(filename,"r") #opens file 
    dna = txt_file.read() #reads through file
    dna_list = dna.split("\n") #creates string in list for every new line
    del dna_list[-1] #removes last string (which is an empty/None string)
    txt_file.close()
    return dna_list

def assemble_genome2(dna_list):
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
    for i in range(1,min(min(len(str1),len(str2)),8)+1): #check each segment to see if overlap works
        if (str1[0-i:] == str2[:i]): #check the overlap segment
            overlap = i #set the max overlap
    return overlap #return the max value
