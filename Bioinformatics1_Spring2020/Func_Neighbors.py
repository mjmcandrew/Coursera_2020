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

results = Neighbors('CATACGTT', 3)
newresults = [str(a) for a in results]
print(" " . join(newresults))
