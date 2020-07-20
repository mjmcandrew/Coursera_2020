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
