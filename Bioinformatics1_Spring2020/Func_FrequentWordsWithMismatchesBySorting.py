def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns ← an empty set
    Neighborhoods ← an empty list
    for i ← 0 to |Text| − k
        add Neighbors(Text(i, k), d) to Neighborhoods
    form an array NeighborhoodArray holding all strings in Neighborhoods
    for i ← 0 to |Neighborhoods| − 1
        Pattern ← NeighborhoodArray(i)
        Index(i) ← PatternToNumber(Pattern)
        Count(i) ← 1
    SortedIndex ← Sort(Index)
    for i ← 0 to |Neighborhoods| − 2
        if SortedIndex(i) = SortedIndex(i + 1)
            Count(i + 1) ← Count(i) + 1
   maxCount ← maximum value in array Count
   for i ← 0 to |Neighborhoods| − 1
       if Count(i) = maxCount
           Pattern ← NumberToPattern(SortedIndex(i), k)
           add Pattern to FrequentPatterns
   return FrequentPatterns


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
