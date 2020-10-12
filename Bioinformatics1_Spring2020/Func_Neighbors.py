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

results = Neighbors('CATACGTT', 3)
newresults = [str(a) for a in results]
print(" " . join(newresults))
