def ClumpFinding(genome, k, L, t):
    #This function finds kmers of size 'k' which form clumps (i.e. they occur
    #at minimum t times in a region of length L).
    frequentPatterns = []
    #Initializes the empty list 'frequentPatterns'.
    clumps = [0] * (4 ** k)
    #Initializes an array containing a count of 0 for all possible kmers
    #of length k, where the index refers to a kmer based on its lexographic
    #position among possible kmers.
    for character in range(len(genome) - k + 1):
        #Iterates through each character in genome accounting for length 'k'.
        text = genome[character:character+L]
        #Captures text in the range of input length 'L'.
        frequencyArray = computing_frequencies(text, k)
        #Computes frequencies for each pattern present in the portion of the
        #genome of length L.
        for index in range(len(frequencyArray)):
            #Iterates through the frequencyArray.
            if frequencyArray[index] >= t:
                #If the pattern occurs 't' times or more, the pattern is marked
                #as a potential clump in 'clumps'.
                clumps[index] = 1
        for index in range(len(clumps)):
            #Iterates through clumps.
            if clumps[index] == 1:
                #If the pattern present at this position in 'clumps' occurs
                #greater than or equal to 't' times in a segment of length 'L'
                #(marked by the presence of a 1), the index position is
                #converted back to its representative pattern and added
                #to frequentPatterns if not already present.
                pattern = NumberToPattern(index, k)
                if pattern not in frequentPatterns:
                    frequentPatterns.append(pattern)
    return frequentPatterns
#This function now works, but it is inefficient. See the BetterClumpFinding
#function for an improved version.

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
