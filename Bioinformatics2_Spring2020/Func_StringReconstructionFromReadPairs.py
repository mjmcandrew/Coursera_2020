def StringReconstructionFromReadPairs(ReadPairs, k, d):
    deBruijn = deBruijnFromReadPairs(ReadPairs)
    path = EulerianPath(deBruijn)
    formatted_path = formatReadPairEulerianPath(path)
    stringReconstruction = StringSpelledByGappedPatterns(formatted_path, k, d)
    return stringReconstruction

def deBruijnFromReadPairs(GappedPatterns):
    deBruijnGraph = {}
    #Creates the empty dictionary deBruijnGraph.
    #Have to update this such that I am considering both list[0] and list[1]
    for pattern in GappedPatterns:
        read_key = ('|').join(pattern)
        deBruijnGraph[read_key] = []
    for pattern in GappedPatterns:
        #Iterates through patterns in the input 'Patterns'.
        k_length = len(pattern[0])
        read1_fwd = pattern[0]
        read1_rev = pattern[1]
        #Sets k_length equal to the length of the pattern.
        read1_fwd_suffix = pattern[0][1:]
        read1_rev_suffix = pattern[1][1:]
        read1_key = ('|').join(pattern)
        #Sets the variable 'prefix' equal to the first through the penultimate character in the string
        #'pattern'.
        for pattern2 in GappedPatterns:
            read2_fwd = pattern2[0]
            read2_rev = pattern2[1]
            read2_fwd_prefix = pattern2[0][0:k_length - 1]
            read2_rev_prefix = pattern2[1][0:k_length - 1]
            read2_key = ('|').join(pattern2)
            if read1_fwd_suffix == read2_fwd_prefix and read1_rev_suffix == read2_rev_prefix:
                if read1_key not in deBruijnGraph:
                    deBruijnGraph[read1_key] = [read2_key]
                else:
                    deBruijnGraph[read1_key].append(read2_key)
    return deBruijnGraph

def EulerianPath(graph):
    degrees = countDegrees(graph)
    #Determine start node and end node based on Eulerian principles.
    for node in degrees:
        if (degrees[node][0] - degrees[node][1]) == 1:
            start_node = node
        elif (degrees[node][1] - degrees[node][0]) == 1:
            end_node = node
    if not start_node or not end_node:
        return "Graph is not Eulerian!"
    if end_node not in graph.keys():
        graph[end_node] = [start_node]
    else:
        graph[end_node].append(start_node)
    path = []
    cycle = []
    path.append(start_node)
    current_node = start_node
    while path:
        if graph[current_node]:
            neighbor = graph[current_node].pop()
            current_node = neighbor
            path.append(current_node)
        else:
            cycle.append(path.pop())
            if path:
                current_node = path[-1]
    cycle = cycle[::-1]
    cycle.pop()
    return cycle

def countDegrees(graph):
    degrees = {}
    for key in graph:
        degrees[key] = []
        degrees[key].append(len(graph[key]))
        degrees[key].append(0)
        #This determines outdegree and sets it at degrees[key][0]. It then appends a placeholder 0
        #in degrees[key][1] for indegree.
    for key in graph:
        for value in graph[key]:
            if value not in degrees.keys():
                degrees[value] = [0, 1]
            else:
                degrees[value][1] += 1
        #This determines indegree and also accounts for any nodes which only have indegrees and 0
        #outdegrees.
    return degrees

def formatReadPairEulerianPath(path):
    formatted_pairs = []
    for node in path:
        formatted_pairs.append(node.split('|'))
    return formatted_pairs

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

import random

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

k = 3
d = 1
with open("StringReconstructionReadPairs.txt") as f:
    input = f.readlines()
    gapped_patterns =[x.strip() for x in input]
    GappedPatterns = []
    for pattern in gapped_patterns:
        GappedPatterns.append(pattern.split('|'))
graph = deBruijnFromReadPairs(GappedPatterns)
handwritten_graph = {'ACC|ATA': ['CCG|TAC'], 'ACT|ATT': ['CTG|TTC'], 'ATA|TGA': ['TAC|GAT'], 'ATT|TGA': ['TTC|GAA'], 'CAC|GAT':['ACC|ATA', 'ACT|ATT'], 'CCG|TAC': ['CGA|ACT'], 'CGA|ACT': ['GAA|CTT', 'GAT|CTG', 'GAT|CTG'], 'CTG|AGC': ['TGA|GCT'], 'CTG|TTC': ['TGA|TCT'], 'GAA|CTT': [], 'GAT|CTG': ['ATA|TGA', 'ATT|TGA'], 'TAC|GAT': ['ACC|ATA', 'ACT|ATT'], 'TCT|AAG': ['CTG|AGC'], 'TGA|GCT': ['GAA|CTT', 'GAT|CTG'], 'TGA|TCT': ['GAA|CTT', 'GAT|CTG'], 'TTC|GAA': ['TCT|AAG']}
print('graph is :\n')
for key, value in graph.items():
    print(key + ' -> ' + ','.join(map(str, value)))
print('handwritten_graph is:\n')
for key, value in handwritten_graph.items():
    print(key + ' -> ' + ','.join(map(str, value)))
degrees = countDegrees(graph)
handwritten_degrees = countDegrees(handwritten_graph)
print('degrees are :\n', degrees)
print('handwritten degrees are:\n', handwritten_degrees)
print('Eulerian Cycle is ', EulerianCycle(graph))
print(StringReconstructionFromReadPairs(GappedPatterns, k, d))
