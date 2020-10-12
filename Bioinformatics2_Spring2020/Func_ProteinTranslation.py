def ProteinTranslation(pattern):
    #This algorithm translates an RNA string 'pattern' into its
    #corresponding amino acid string peptide.
    codons = generateCodons(pattern)
    #Generates in-frame codons from input 'pattern'.
    protein = ''
    #Initializes the empty string 'protein'.
    for codon in codons:
        #Iterates through codons generated using the generateCodons
        #subfunction.
        amino_acid = codonDict[codon]
        if amino_acid != 'STOP':
            protein += amino_acid
        else:
            return protein
        #This if/else check continues to add amino acids to the protein string
        #as long as the codon codes for an amino acid, and not the stop codon.
        #When the loop encounters a stop codon, it returns the protein string
        #constructed up to that point.
    return protein

def generateCodons(pattern):
    #This algorithm generates all codons from an input RNA string
    #'pattern' in frame (i.e. pattern[0:3] = codon1, etc.).
    pattern_length = len(pattern)
    kmer_list = []
    index = 0
    while index in range(pattern_length - 2):
        kmer = pattern[index:index + 3]
        kmer_list.append(kmer)
        index += 3
    return kmer_list




codonDict = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M', 'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E', 'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': 'STOP', 'UAC': 'Y', 'UAG': 'STOP', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 'UGA': 'STOP', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L', 'UUU': 'F'}
