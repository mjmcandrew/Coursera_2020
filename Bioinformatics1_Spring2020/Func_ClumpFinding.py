def ClumpFinding(genome, k, L, t):
    frequentPatterns = []
    clumps = [0] * (4 ** k)
    for character in range(len(genome) - k + 1):
        text = genome[character:character+L]
        frequencyArray = computing_frequencies(text, k)
        for index in range(len(frequencyArray)):
            if frequencyArray[index] >= t:
                clumps[index] = 1
        for index in range(len(clumps)):
            if clumps[index] == 1:
                pattern = NumberToPattern(index, k)
                if pattern not in frequentPatterns:
                    frequentPatterns.append(pattern)
    return frequentPatterns
#This function now works, but it is inefficient. See the BetterClumpFinding
#function for an improved version.
def computing_frequencies(Text, k):
    frequencyArray = [0] * ((4 ** k))
    for character in range(len(Text) - (k - 1)):
        pattern = Text[character:character+k]
        index = PatternToNumber(pattern)
        frequencyArray[index] = frequencyArray[index] + 1
    return frequencyArray

def NumberToPattern(index, kLength):
    base4string = {}       # This creates the dictionary that will be used to
    base4string[0] = 'A'   # convert a base 4 number to a DNA string.
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
