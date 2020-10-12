def MinimumSkew(Genome):
    positions = []
    #Initializes the empty list 'positions' which will record index positions
    #with minimum skew.
    skewList = SkewArray(Genome)
    #Computes the skew array for the entire input Genome.
    skewMin = max(skewList)
    #Finds the maximum value in the skew array, which paradoxically
    #represents the minimum skew because of the way guanine is scored.
    for index in range(len(skewList)):
        if skewList[index] == skewMin:
            positions.append(index)
    #The above iterates through the skew array and records the positions
    #where minimum skew is observed in the list 'positions'.
    return positions

def SkewArray(Genome):
    #This algorithm computes an array of the 'skew' of a genome; that is,
    #the relationship between the number of guanines and cytosines. Cytosine
    #can deaminate into thymine, and this process is made more likely when
    #a stretch of DNA is in single-stranded form. Skew tends to decrease along
    #the reverse half-strand and increase along the forward half-strand around
    #origins of replication in bacterial genomes, since these areas spend more
    #time as ssDNA than the rest of the genome.
    skew = [''] * (len(Genome) + 1)
    #Creates an empty array, with each index position corresponding to the
    #an index position in the genome. The empty string will be replaced by
    #a running skew value as we iterate through 'Genome'.
    skew[0] = 0
    #Initials the value of the first position in the skew array to 0.
    skewValue = 0
    n = len(Genome)
    for index in range(n):
        #Iterates through indices the length of the genome.
        if Genome[index] == 'G':
            #If the character at an index is a guanine, the skewValue is
            #increased, and the skew array at the next index position (because
            #the first position (0) should have an initial value of 0) is
            #updated with the current running value.
            skewValue += 1
            skew[index + 1] = skewValue
        if Genome[index] == 'C':
            #See above for == 'G'.
            skewValue -= 1
            skew[index + 1] = skewValue
        else:
            #If the algorithm encounters an 'A' or 'T', the skew value does
            #not change, but the position is still assigned the current skew
            #value.
            skew[index + 1] = skewValue
    return skew
