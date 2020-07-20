def DistanceBetweenPatternAndStrings(pattern, Dna):
    k = len(pattern)
    #Initializes a variable 'k' that is equal to the length of input 'pattern'.
    distance = 0
    #Sets initial distance to 0.
    for Dna_string in Dna:
        #Iterates through strings in the set 'Dna'.
        string_length = len(Dna_string)
        #Sets 'string_length' to the length of the current string in the list 'Dna'.
        Hamming = float('inf')
        #Sets the initial Hamming distance to infinity.
        for index in range(string_length - k + 1):
            #Iterates through each position in each string allowing for the
            #length of the kmer 'pattern'.
            possible_match = Dna_string[index:index+k]
            #Obtains potential matches of size 'k' to match 'pattern'.
            match_distance = HammingDistance(pattern, possible_match)
            #Finds the HammingDistance between 'pattern' and the possible
            #match.
            if Hamming > match_distance:
                Hamming = match_distance
                #If the distance between 'pattern' and its potential match
                #is less than the current Hamming Distance, replaces Hamming
                #with the distance between 'pattern' and potential match.
        distance = distance + Hamming
        #Replaces distance (initially set to 0) with the current value of
        #'distance' plus the current value of Hamming.
    return distance

def HammingDistance(p, q):
    distance = 0
    #Sets initial distance to 0.
    for index in range(len(p)):
        #Iterates through the nucleotide at each index in the
        #kmer 'p'.
        if p[index] == q[index]:
            #Checks whether the nucleotides at each index are the
            #same in both p and q.
            distance = distance
            #If this is the case, the distance between the two
            #kmers does not change.
        else:
            distance += 1
            #If the nucleotides at a particular index are different,
            #this increases the Hamming distance by 1.
    return distance
