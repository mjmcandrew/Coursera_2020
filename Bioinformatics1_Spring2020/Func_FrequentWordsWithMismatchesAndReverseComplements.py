def FrequentWordsWithMismatchesAndReverseComplements(text, k, d):
    words = []
    #Initializes the empty list 'words' which will store frequent patterns
    #accounting for mismatches, as well as the reverse complement of the input
    #string text.
    freq = ComputingFrequenciesWithMismatches(text, k, d)
    #Computes the frequency array.
    m = max(freq)
    #Finds the maximum frequency value in the array.
    for index in range(len(freq)):
        #Iterates through the frequency array. If the value assigned to an index
        #matches the maximum, the index is converted back to its corresponding
        #pattern, and this pattern is added to 'words'.
        if freq[index] == m:
            Pattern = NumberToPattern(index, k)
            words.append(Pattern)
    return words

def ComputingFrequenciesWithMismatches(Text, k, d):
    #This algorithm computes the frequency with which patterns of length 'k' occur
    #in the string 'Text', while allowing for 'd' mismatches.
    FrequencyArray = [0] * (4 ** k)
    #Initializes the frequency array with placeholder 0's for each possible kmer.
    for index in range(len(Text) - k + 1):
        #Iterates through indices in 'Text' with regard to 'k'.
        Pattern = Text[index:index+k]
        #Captures the pattern of length 'k' present at the current index.
        Neighborhood = Neighbors(Pattern, d)
        #Calculates all neighbors of the current pattern using the helper algorithm
        #Neighbors.
        for ApproximatePattern in Neighborhood:
            #Converts all patterns calculated above to numbers and increments
            #the frequency value of the corresponding index.
            FrequencyArrayIndex = PatternToNumber(ApproximatePattern)
            FrequencyArray[FrequencyArrayIndex] += 1
    return FrequencyArray

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

def NumberToPattern(index, kLength):
    base4string = {}
    base4string[0] = 'A'
    base4string[1] = 'C'
    base4string[2] = 'G'
    base4string[3] = 'T'
    #The above lines create a dictionary that will be used to convert
    #numbers to DNA strings.
    remainder = 0
    base4pattern = ''
    count = 0
    while count < kLength:
        quotient = int(index / 4)
        remainder = int(index % 4)
        base4pattern = base4string[remainder] + base4pattern
        count += 1
        index = quotient
    #The above portion of the algorithm iteratively divides the number
    #representing a pattern by 4 and adds the character represented by
    #the remainder to the pattern string. In essence, this is algorithm
    #converts a base4 number back to a string of nucleotides.
    return base4pattern

def PatternToNumber(pattern):
    base4 = {}
    base4['A'] = 0
    base4['C'] = 1
    base4['G'] = 2
    base4['T'] = 3
    #The above lines create the dictionary that will be used to convert each
    #base to a number.
    n = len(pattern)
    number = 0
    if n == 0: #Ensures that user has entered a DNA base string.
        return "You have not entered a string."
    for character in range(n):
        #Iterates through each character in the DNA string.
        number += base4[pattern[character]] * (4 ** (n - character - 1))
        # Note: "character" is required as part of the "n - ..." equation
        # because "character" acquires the index value of the character inside
        # the string. For instance, in a string "AGT", character would be
        # assigned as A = 0, G = 1, T = 2, while the value of n does not
        # change.
    return number

def ReverseComplement(Pattern):
    #Utilizes the Reverse and Complement functions to generate the
    #reverse complement of a DNA string 'Pattern'.
    revComp = ''
    rev = Reverse(Pattern)
    revComp = Complement(rev)
    return revComp

def Reverse(Pattern):
    #Generates the reverse of input string 'Pattern' such that it is
    #the same string read 3' to 5'.
    reverse = ''
    for character in Pattern:
        reverse = character + reverse
    return reverse

def Complement(Pattern):
    #Finds the complement of a DNA string 'Pattern' based on Mendelian
    #base-pairing.
    comp = {}
    comp['A'] = 'T'
    comp['C'] = 'G'
    comp['G'] = 'C'
    comp['T'] = 'A'
    complementPattern = ''
    for character in Pattern:
        complementPattern = complementPattern + comp[character]
    return complementPattern
