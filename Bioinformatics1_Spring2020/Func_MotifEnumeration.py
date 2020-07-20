def MotifEnumeration(Dna, k, d):
    Patterns = []
    for Dna_string in Dna:
        city = build_city(Dna_string, k, d)
        for Neighbor in city:
            check = check_potential_match(Dna, Neighbor, k, d)
            if check == True:
                if Neighbor not in Patterns:
                    Patterns.append(Neighbor)
    return Patterns

def check_potential_match(Dna, Neighbor, k, d):
    for inner_Dna_string in Dna:
        potential_match = find_potential_match(inner_Dna_string, Neighbor, k, d)
        if potential_match == False:
            return False    #go to "For Neighbor in city...."
    return True

def find_potential_match(inner_Dna_string, Neighbor, k, d):
    motif_length = len(inner_Dna_string)
    for index in range(motif_length-k+1):
        potential_match = inner_Dna_string[index:index+k]
        if HammingDistance(Neighbor, potential_match) <= d:
            return True
    return False

def build_city(Dna_string, k, d):
    city = []
    motif_length = len(Dna_string)
    for index in range(motif_length-k+1):
            Pattern = Dna_string[index:index+k]
            Neighborhood = Neighbors(Pattern, d)
            city.append(Pattern)
            for Neighbor in Neighborhood:
                city.append(Neighbor)
    return city

def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    Neighborhood = []
    nucleotides = ['A', 'C', 'G', 'T']
    firstSymbol = Pattern[0]
    Suffix = Pattern[1:]
    SuffixNeighbors = Neighbors(Suffix, d)
    for item in SuffixNeighbors:
        if HammingDistance(Suffix, item) < d:
            for character in nucleotides:
                newNeighbor = character + item
                Neighborhood.append(newNeighbor)
        else:
            newNeighbor = firstSymbol + item
            Neighborhood.append(newNeighbor)
    return Neighborhood

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
