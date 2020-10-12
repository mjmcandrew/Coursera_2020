def PeptideEncoding(Text, Peptide):
    #This algorithm finds all kmers present in a string 'text' which may encode
    #the input 'Peptide' on either the forward or reverse strand.
    peptideEncoding_kmers = []
    #Initializes empty list 'peptideEncoding_kmers'.
    rev_complement = ReverseComplement(Text)
    fwd_transcript = generateTranscript(Text)
    rev_transcript = generateTranscript(rev_complement)
    #The above lines generate the reverse complement of the input 'Text',
    #then transcribe both strands into mRNA by replacing thymine with
    #uridine.
    peptide_length = len(Peptide)
    #Assigns the length of the peptide to 'peptide_length'.
    k = (3 * peptide_length)
    #Assigns a value of 3 times peptide_length to the variable 'k' to
    #account for codon size.
    fwd_pep_length_kmers = StringComposition(fwd_transcript, k)
    fwd_matches = kmerPeptideMatching(Peptide, fwd_pep_length_kmers)
    rev_pep_length_kmers = StringComposition(rev_transcript, k)
    rev_matches = kmerPeptideMatching(Peptide, rev_pep_length_kmers)
    #The above lines generate all peptide-length kmers present in the
    #forward and reverse transcripts using StringComposition, then determines
    #if any of these kmers translate to the input 'Peptide' using
    #kmerPeptideMatching.
    for match in rev_matches:
        peptideEncoding_kmers.append(ReverseComplement(match))
        #Iterates through matches present on the reverse strand and generates
        #their reverse complements in order to reflect the kmer actually
        #present in the input strand 'Text'.
    peptideEncoding_kmers = fwd_matches + peptideEncoding_kmers
    return peptideEncoding_kmers

def kmerPeptideMatching(Peptide, kmers):
    #This sub-algorithm
    matches = []
    for kmer in kmers:
        translation = ProteinTranslation(kmer)
        if translation == Peptide:
            matches.append(reverseTranscribe(kmer))
    return matches

def generateTranscript(Pattern):
    #This transcribes DNA to mRNA by replacing thymine with uridine.
    transcript = Pattern.replace('T', 'U')
    return transcript

def reverseTranscribe(Pattern):
    #This reverse transcribes an RNA string back to its DNA counterpart by
    #replacing uridine with thymine in the string.
    reverse_transcript = Pattern.replace('U', 'T')
    return reverse_transcript

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

def StringComposition(Text, k):
    #This algorithm returns all patterns of length 'k' present in input
    #'Text' sorted lexographically.
    string_length = len(Text)
    kmer_list = []
    for index in range(string_length - k + 1):
        kmer = Text[index:index + k]
        kmer_list.append(kmer)
    kmer_list.sort()
    return kmer_list

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
with open("Bacillus_brevis.txt") as f:
    input = f.readlines()
    print(input)
    stripped_input = [x.strip() for x in input]
    pattern = ''.join(stripped_input)

peptide = 'VKLFPWFNQY'

result = PeptideEncoding(pattern, peptide)
for kmer in result:
    print(kmer)
print(len(result))
