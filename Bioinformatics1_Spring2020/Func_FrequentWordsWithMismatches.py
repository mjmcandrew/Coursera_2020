def FrequentWordsWithMismatches(Text, k, d):
    positions = []
    for index in range(len(Genome)-len(Pattern)+1):
        if HammingDistance(Genome[index:index+len(Pattern)], Pattern) <= d:
            positions.append(index)
    return positions

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

newresults = [str(a) for a in results]
print(" " . join(newresults))
