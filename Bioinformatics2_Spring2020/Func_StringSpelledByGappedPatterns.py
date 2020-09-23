def StringSpelledByGappedPatterns(GappedPatterns, k, d):
    FirstPatterns = []
    SecondPatterns = []
    for pattern in GappedPatterns:
        FirstPatterns.append(pattern[0])
        SecondPatterns.append(pattern[1])
    PrefixString = PathToGenome(FirstPatterns)
    SuffixString = PathToGenome(SecondPatterns)
    for index in range((k + d), len(PrefixString)):
        if PrefixString[index] != SuffixString[index - k - d]:
            return "There is no string spelled by the gapped patterns!"
    return PrefixString + SuffixString[-(k+d):]

def PathToGenome(Patterns):
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
