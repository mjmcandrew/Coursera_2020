def MotifEnumeration(Dna, k, d):
    #Given a collection of strings 'Dna', this algorithm finds motifs of size
    #'k' which are common to all strings, allowing for mismatches 'd'.
    Patterns = []
    #Initializes the empty list 'Patterns'.
    for Dna_string in Dna:
        #Iterates through individual strings in the input 'Dna'.
        city = build_city(Dna_string, k, d)
        #Utilizes the 'build_city' helper algorithm to capture all patterns in
        #the string, as well as the neighbors of that pattern differing by at
        #most 'd' mismatches.
        for Neighbor in city:
            #Iterates through captured patterns and its relatives.
            check = check_potential_match(Dna, Neighbor, k, d)
            #Utilizes the 'check_potential_match' helper algorithm to determine
            #whether the current pattern appears
            if check == True:
                if Neighbor not in Patterns:
                    Patterns.append(Neighbor)
    return Patterns

def check_potential_match(Dna, Neighbor, k, d):
    #This helper algorithm goes through remaining DNA strings in the input Dna
    #and determines whether there are patterns which match potential motifs by
    #at most distance 'd'.
    for inner_Dna_string in Dna:
        potential_match = find_potential_match(inner_Dna_string, Neighbor, k, d)
        if potential_match == False:
            return False
    return True

def find_potential_match(inner_Dna_string, Neighbor, k, d):
    #Similar to the 'build_city' helper algorithm, except that this algorithm
    #accepts an input pattern as a potential match, then determines whether there
    #is a pattern present in the current DNA string differing from that pattern
    #by at most 'd'.
    motif_length = len(inner_Dna_string)
    for index in range(motif_length-k+1):
        potential_match = inner_Dna_string[index:index+k]
        if HammingDistance(Neighbor, potential_match) <= d:
            return True
    return False

def build_city(Dna_string, k, d):
    #This algorithm iterates through a DNA string and finds all patterns of length
    #k present in that string, as well as all neighbors differing from these patterns
    #by at most distance d.
    city = []
    #Initializes empty list 'city'.
    motif_length = len(Dna_string)
    #Establishes variable 'motif_length' as the length of the input DNA string.
    for index in range(motif_length-k+1):
        #Iterates through indices in the DNA string.
            Pattern = Dna_string[index:index+k]
            #Captures each pattern of length k.
            Neighborhood = Neighbors(Pattern, d)
            #Computes neighbors of each pattern in the DNA string.
            city.append(Pattern)
            #Adds both the pattern and its neighbors to the list 'city'.
            for Neighbor in Neighborhood:
                city.append(Neighbor)
    return city

def Neighbors(Pattern, d):
    #This algorithm returns all strings related to input 'Pattern' which
    #differ from that pattern by at most distance 'd' (# of mismatches).
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    #The above lines establish the base cases for the recursive portion
    #of the algorithm below.
    Neighborhood = []
    #Initializes the empty list 'Neighborhood'.
    nucleotides = ['A', 'C', 'G', 'T']
    firstSymbol = Pattern[0]
    #Initializes the variable 'firstSymbol' as the first character in the
    #input string 'Pattern'.
    Suffix = Pattern[1:]
    #Stores the remaining characters in 'Pattern' as the suffix.
    SuffixNeighbors = Neighbors(Suffix, d)
    #Recursively calls Neighbors on suffix allowing for 'd' mismatches.
    for item in SuffixNeighbors:
        #Iterates through items in 'SuffixNeighbors'.
        if HammingDistance(Suffix, item) < d:
            for character in nucleotides:
                newNeighbor = character + item
                Neighborhood.append(newNeighbor)
        else:
            newNeighbor = firstSymbol + item
            Neighborhood.append(newNeighbor)
    return Neighborhood

def HammingDistance(p, q):
    #This algorithm determines the number of mismatches (Hamming Distance)
    #between two input strings 'p' and 'q'.
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
