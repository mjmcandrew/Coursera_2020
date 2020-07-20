def FasterFrequentWordsWithMismatches(Text, k, d):
    words = []
    freq = ComputingFrequenciesWithMismatches(Text, k, d)
    m = max(freq)
    for index in range(len(freq)):
        if freq[index] == m:
            Pattern = NumberToPattern(index, k)
            words.append(Pattern)
    return words

def ComputingFrequenciesWithMismatches(Text, k, d):
    FrequencyArray = [0] * (4 ** k)
    for index in range(len(Text) - k + 1):
        Pattern = Text[index:index+k]
        Neighborhood = Neighbors(Pattern, d)
        for ApproximatePattern in Neighborhood:
            FrequencyArrayIndex = PatternToNumber(ApproximatePattern)
            FrequencyArray[FrequencyArrayIndex] += 1
    return FrequencyArray

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

def PatternToNumber(pattern):
    base4 = {}       # This creates the dictionary that will be used to convert
    base4['A'] = 0   # a DNA base string to a number.
    base4['C'] = 1
    base4['G'] = 2
    base4['T'] = 3
    n = len(pattern)
    number = 0
    if n == 0: #Ensures that user has entered a DNA base string.
        return "You have not entered a string."
    for character in range(n):
        number += base4[pattern[character]] * (4 ** (n - character - 1))
        # Note: "character" is required as part of the "n - ..." equation
        # because "character" acquires the index value of the character inside
        # the string. For instance, in a string "AGT", character would be
        # assigned as A = 0, G = 1, T = 2, while the value of n does not
        # change.
    return number

def NumberToPattern(index, kLength):
    base4string = {}       # This creates the dictionary that will be used to convert
    base4string[0] = 'A'   # a base 4 number to a DNA string.
    base4string[1] = 'C'
    base4string[2] = 'G'
    base4string[3] = 'T'
    remainder = 0
    base4pattern = ''
    count = 0
    while count < kLength:
        quotient = int(index / 4)
        remainder = int(index % 4)
        base4pattern = base4string[remainder] + base4pattern
        count += 1
        index = quotient
    return base4pattern
