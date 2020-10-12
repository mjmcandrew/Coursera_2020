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

print(PatternToNumber('ACGT'))
