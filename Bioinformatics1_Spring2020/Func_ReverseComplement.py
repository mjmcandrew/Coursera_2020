def ReverseComplement(Pattern):
    revComp = ''
    rev = Reverse(Pattern)
    revComp = Complement(rev)
    return revComp

def Reverse(Pattern):
    reverse = ''
    for character in Pattern:
        reverse = character + reverse
    return reverse

def Complement(Pattern):
    comp = {}
    comp['A'] = 'T'
    comp['C'] = 'G'
    comp['G'] = 'C'
    comp['T'] = 'A'
    complementPattern = ''
    for character in Pattern:
        complementPattern = complementPattern + comp[character]
    return complementPattern
