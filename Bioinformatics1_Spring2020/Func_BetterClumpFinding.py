def BetterClumpFinding(genome, k, L, t):
    #This algorithm improves on the ClumpFinding algorithm by computing the frequency
    #array only once, and updating it as the window slides through the genome.
    frequentPatterns = []
    #Initializes the empty list 'frequentPatterns'.
    clumps = [0] * (4 ** k)
    #Initializes the list 'clumps' with placeholder 0's for all potential patterns
    #of length k.
    text = genome[0:L]
    frequencyArray = computing_frequencies(text, k)
    #Generates the frequency array.
    for index in range(len(frequencyArray)):
        if frequencyArray[index] >= t:
            #Iterates through the frequency array and identifies patterns which
            #occur greater than or equal to 't' times and increments the value
            #associated with the pattern by 1 in 'clumps'.
            clumps[index] = 1
    for index in range(len(genome) - L):
        #This iterates through the genome, accounting for the length of 'L' and
        #updates the frequency array accordingly, while checking whether the
        #patterns identified in the window of length 'L' meet the criteria of
        #occurring 't' times. If the patterns do occur 't' or more times, their
        #frequency is updated in 'clumpes'.
        firstPattern = genome[index:index+k]
        firstPatternIndex = PatternToNumber(firstPattern)
        frequencyArray[firstPatternIndex] -= 1
        lastPattern = genome[(index+L-k):index+L]
        lastPatternIndex = PatternToNumber(lastPattern)
        frequencyArray[lastPatternIndex] += 1
        if frequencyArray[firstPatternIndex] >= t:
            clumps[firstPatternIndex] = 1
        if frequencyArray[lastPatternIndex] >= t:
            clumps[lastPatternIndex] = 1
    for index in range(len(clumps)):
        #Iterates through clumps and finds patterns which have been assigned a
        #frequency of 1, meaning that they occur 't' or more times in a window
        #of length l. If so, they are added to the list 'frequentPatterns'.
        if clumps[index] == 1:
            pattern = NumberToPattern(index, k)
            frequentPatterns.append(pattern)
    return frequentPatterns

def computing_frequencies(Text, k):
    #This algorithm computes the frequencies of all kmers of length 'k'
    #that are present in input 'Text'
    frequencyArray = [0] * ((4 ** k))
    #Initializes an array containing a count of 0 for all possible kmers
    #of length k, where the index refers to a kmer based on its lexographic
    #position among possible kmers.
    for character in range(len(Text) - (k - 1)):
        #Iterates through 'Text' accounting for length of 'k'.
        pattern = Text[character:character+k]
        #Captures the pattern of length 'k' at each position.
        index = PatternToNumber(pattern)
        #Determines the index of the pattern based on the PatternToNumber
        #algorithm.
        frequencyArray[index] = frequencyArray[index] + 1
        #Increments the frequency associated with the pattern by 1.
    return frequencyArray

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
    if n == 0:
        #Ensures that user has entered a DNA base string.
        return "You have not entered a string."
    for character in range(n):
        #Iterates through each character in the DNA string.
        number += base4[pattern[character]] * (4 ** (n - character - 1))
        #Note: "character" is required as part of the "n - ..." equation
        #because "character" acquires the index value of the character inside
        #the string. For instance, in a string "AGT", character would be
        #assigned as A = 0, G = 1, T = 2, while the value of n does not
        #change.
    return number
