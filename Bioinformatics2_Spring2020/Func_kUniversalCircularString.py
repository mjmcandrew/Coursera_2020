import itertools
import random

def kUniversalCircularString(k):
    binary_strings = generateBinaryStrings(k)
    binary_deBruijn = deBruijnFromKmers(binary_strings)
    binary_cycle = EulerianCycle(binary_deBruijn)
    circular_string = PathToGenome(binary_cycle)
    return circular_string[: len(circular_string) - k + 1]

def generateBinaryStrings(k):
    binary = ['0', '1']
    binary_strings = [''.join(p) for p in itertools.product(binary, repeat=k)]
    return binary_strings

def deBruijnFromKmers(Patterns):
    deBruijnGraph = {}
    #Creates the empty dictionary deBruijnGraph.
    for pattern in Patterns:
        #Iterates through patterns in the input 'Patterns'.
        k_length = len(pattern)
        #Sets k_length equal to the length of the pattern.
        suffix = pattern[1:]
        #Sets the variable 'suffix' equal to the second through final character in the string 'pattern'.
        prefix = pattern[0: k_length - 1]
        #Sets the variable 'prefix' equal to the first through the penultimate character in the string
        #'pattern'.
        if prefix not in deBruijnGraph:
            deBruijnGraph[prefix] = []
            #Creates an empty list as a value assigned to the key for the specified prefix.
            deBruijnGraph[prefix].append(suffix)
            #Adds the pattern's suffix to the list value associated with this prefix key.
        else:
            deBruijnGraph[prefix].append(suffix)
            #If the prefix key already exists in the dictionary, this simply appends the suffix that follows.
    return deBruijnGraph

def EulerianCycle(graph):
    cycle = []
    path = []
    current_node = random.choice(list(graph))
    path.append(current_node)
    while path:
        if graph[current_node]:
            neighbor = graph[current_node].pop()
            current_node = neighbor
            path.append(current_node)
        else:
            cycle.append(path.pop())
            if path:
                current_node = path[-1]
    return cycle[::-1]

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

print(kUniversalCircularString(9))
