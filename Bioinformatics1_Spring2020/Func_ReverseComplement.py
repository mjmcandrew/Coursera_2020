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
