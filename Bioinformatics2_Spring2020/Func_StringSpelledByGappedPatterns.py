def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    #This algorithm takes as input read pairs in the format [['read1, read2'], etc]
    #as well as a value 'k' (the length of each read in the read pair) and
    #distance 'd' which separates read1 from read2. The output is the string
    #reconstructed from these read pairs, if such a string exists. Note that
    #the input read pairs may have to be formatted before input from ['read1|read2', etc.].
    FirstPatterns = []
    SecondPatterns = []
    for pattern in GappedPatterns:
        #Iterates through patterns in the list of lists 'GappedPatterns'.
        FirstPatterns.append(pattern[0])
        SecondPatterns.append(pattern[1])
        #Stores read1 in the list 'FirstPatterns' and read2 in the list 'SecondPatterns'.
    PrefixString = PathToGenome(FirstPatterns)
    #Reconstructs a string from all first reads present in input.
    SuffixString = PathToGenome(SecondPatterns)
    #Reconstructs a string from all second reads present in input.
    for index in range((k + d), len(PrefixString)):
        #Determines whether prefix and suffix strings overlap appropriately.
        if PrefixString[index] != SuffixString[index - k - d]:
            return "There is no string spelled by the gapped patterns!"
    #If the strings overlap appropriately, the strings are joined, accounting
    #for the lengths of k and d, and this final string is returned.
    return PrefixString + SuffixString[-(k+d):]

def PathToGenome(Patterns):
    #This algorithm takes an ordered set of kmers and reconstructs them
    #into a continuous string ('genome').
    PathToGenome = Patterns[0]
    #Establishes the first kmer in 'Patterns' as the initial PathToGenome.
    patterns_length = len(Patterns)
    #Determines the number of kmers in 'Patterns'.
    for index in range(1, patterns_length):
        #Iterates through the remaining kmers in 'Patterns'.
        kmer_length = len(Patterns[index])
        #Determines the length of each iterated kmer.
        if Patterns[index][0:kmer_length - 1] == PathToGenome[index:]:
            #Checks whether there is overlap between the final portion of PathToGenome and
            #the initial portion of the kmer string.
            PathToGenome = PathToGenome + Patterns[index][kmer_length - 1]
            #If so, adds the non-overlapping portion of the kmer to PathToGenome.
    return PathToGenome

k = 50
d = 200
with open("StringGappedPatterns.txt") as f:
    input = f.readlines()
    gapped_patterns =[x.strip() for x in input]
    print(gapped_patterns)
    GappedPatterns = []
    for pattern in gapped_patterns:
        GappedPatterns.append(pattern.split('|'))

print(GappedPatterns)
#import sys
#Input = sys.stdin.readline()
#v = Input.strip()
#v = v.split(" ")
#k = int(v[0])
#d = int(v[1])
#Input2 = sys.stdin.readlines()
#gapped_patterns =[x.strip() for x in Input2]
#GappedPatterns = []
#for pattern in gapped_patterns:
    #GappedPatterns.append(pattern.split('|'))
print(StringSpelledByGappedPatterns(GappedPatterns, k, d))
