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
        return "You have not entered a string."
    #Ensures that user has entered a DNA base string.
    for character in range(n):
        #Iterates through each character in the DNA string.
        number += base4[pattern[character]] * (4 ** (n - character - 1))
        # Note: "character" is required as part of the "n - ..." equation
        # because "character" acquires the index value of the character inside
        # the string. For instance, in a string "AGT", character would be
        # assigned as A = 0, G = 1, T = 2, while the value of n does not
        # change.
    return number
