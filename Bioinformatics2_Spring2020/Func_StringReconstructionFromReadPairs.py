def StringReconstructionFromReadPairs(ReadPairs, k, d):
    #This algorithm reconstructs the 'genome' represented by an input set of
    #kmers ('ReadPairs') of length k separated by distance d.
    deBruijn = deBruijnFromReadPairs(ReadPairs)
    #Generates a deBruijn graph from the input 'ReadPairs'.
    path = EulerianPath(deBruijn)
    #Generates a Eulerian path based on the deBruijn graph.
    formatted_path = formatReadPairEulerianPath(path)
    #Formats the Eulerian path such that string reconstruction can be performed.
    stringReconstruction = StringSpelledByGappedPatterns(formatted_path, k, d)
    #Reconstructs the string from the input formatted path, if such a string
    #exists.
    return stringReconstruction

def deBruijnFromReadPairs(GappedPatterns):
    #This algorithm constructs a deBruijn graph from read pairs in the format
    #[[read1, read2], [read1, read2], etc].
    deBruijnGraph = {}
    #Creates the empty dictionary deBruijnGraph.
    for pattern in GappedPatterns:
        #Reformats read pairs such that the key for the read pair in the resulting
        #deBruijn graph looks like 'read1|read2'
        read_key = ('|').join(pattern)
        deBruijnGraph[read_key] = []
        #Initializes outdegree of the read pair to an empty list.
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
            #Performs the same steps as above for all other read pairs in the
            #input GappedPatterns.
            read2_fwd = pattern2[0]
            read2_rev = pattern2[1]
            read2_fwd_prefix = pattern2[0][0:k_length - 1]
            read2_rev_prefix = pattern2[1][0:k_length - 1]
            read2_key = ('|').join(pattern2)
            if read1_fwd_suffix == read2_fwd_prefix and read1_rev_suffix == read2_rev_prefix:
                #If the fwd read in read pair 1's suffix matches the prefix of the
                #fwd read in read pair 2, and the suffix of the rev read in read pair 1
                #matches the prefix of the rev read in read pair 2, the remaining portion
                #adds read2 as an outdegree of read1. If read1 already has an outdegree
                #node, read2 is added to the list of outdegree nodes.
                if read1_key not in deBruijnGraph:
                    deBruijnGraph[read1_key] = [read2_key]
                else:
                    deBruijnGraph[read1_key].append(read2_key)
    return deBruijnGraph

def EulerianPath(graph):
    #This algorithm takes as input a deBruijn graph and returns a Eulerian
    #path (if present) in the graph. A Eulerian path visits each edge in
    #a graph exactly once.
    degrees = countDegrees(graph)
    #Determine start node and end node based on Eulerian principles. In order
    #for a Eulerian path to exist, there must exist a starting node with
    #outdegree one greater than indegree, and an ending node with indegree
    #one greater than outdegree.
    for node in degrees:
        if (degrees[node][0] - degrees[node][1]) == 1:
            start_node = node
        elif (degrees[node][1] - degrees[node][0]) == 1:
            end_node = node
    if not start_node or not end_node:
        return "Graph is not Eulerian!"
    if end_node not in graph.keys():
        #Puts an artificial edge connecting end node and start node in place
        #which will be removed before returning path.
        graph[end_node] = [start_node]
    else:
        graph[end_node].append(start_node)
    path = []
    #Initializes empty list 'path' which will store the current path
    #of nodes visited.
    cycle = []
    #Initializes empty list 'cycle' which will store the Eulerian path.
    path.append(start_node)
    #Adds start node to path.
    current_node = start_node
    #Initiates current_node as the start node.
    while path:
        #Initializes a while loop that will run as long as 'path'
        #is non-empty.
        if node not in graph.keys():
            #If current node is not in the graph's keys (i.e. this node does
            #not have outdegree), the node is added to keys with an empty
            #list as its corresponding value.
            graph[node] = []
        if graph[current_node]:
            #Checks whether the current node has remaining edges connecting
            #to other nodes.
            neighbor = graph[current_node].pop()
            #'Pops' the edge connecting current_node to a neighbor and assigns
            #the neighbor node to variable 'neighbor'.
            current_node = neighbor
            #Reassigns current_node to be neighbor, and adds this node
            #to 'path'.
            path.append(current_node)
        else:
            #If the current node has no remaining edges connecting it to
            #neighbors, the node is removed from path and added to 'cycle'.
            cycle.append(path.pop())
            if path:
                #As long as nodes remain in path, the algorithm backtracks
                #to the previous node and returns to the top of the while loop.
                current_node = path[-1]
    cycle = cycle[::-1]
    cycle.pop()
    #The final value in cycle must be removed, as it is the result of adding
    #an artificial edge between the end node and the start node at the
    #beginning of the algorithm.
    return cycle

def countDegrees(graph):
    #This algorithm iterates through nodes in a graph and determines the
    #indegree and outdegree of each node in the form {node: [outdegree, indegree]}.
    #As a final step, it iterates through values in the graph in order to capture
    #nodes which have no outdegree and assign them an appropriate indegree.
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
    #Since read pairs are in the form 'read1|read2' in the generated Eulerian
    #path, they must be reformatted into a list of lists [['read1', 'read2']]
    #for string reconstruction.
    formatted_pairs = []
    for node in path:
        formatted_pairs.append(node.split('|'))
    return formatted_pairs

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

import random

def EulerianCycle(graph):
    #This algorithm takes as input a deBruijn graph and returns a Eulerian
    #cycle (if present) in the graph. A Eulerian cycle visits each edge in
    #a graph exactly once before returning to the starting node.
    cycle = []
    #Initializes empty list cycle, which will store the final cycle.
    path = []
    #Initializes empty list path, which will store nodes visited nodes
    #in sequential order.
    current_node = random.choice(list(graph))
    #Picks a random node as the starting point.
    path.append(current_node)
    #Appends the starting node to path.
    while path:
        #Initializes a while loop that will run as long as 'path'
        #is non-empty.
        if graph[current_node]:
            #Checks whether the current node has edges which visit other
            #nodes.
            neighbor = graph[current_node].pop()
            #Assigns the node connected via an edge (if present) to the
            #current node to the variable 'neighbor'. The use of 'pop'
            #removes the edge from current node to neighbor. For example,
            #given the node 1 -> 3, 5, 5 will be assigned to 'neighbor'
            #and the resulting entry for node 1 will look like {1: [3]}.
            current_node = neighbor
            #Assigns neighbor as the current node.
            path.append(current_node)
            #Appends the new current_node to path.
        else:
            cycle.append(path.pop())
            #If the current_node does not have any remaining edges
            #connecting it to other nodes, this removes the current
            #node from 'path' using 'pop' and appends it to 'cycle'.
            if path:
                #If 'path' still has nodes in it, this portion of the
                #algorithm backtracks to the most recently visited node
                #and will revert to the top of the while loop with
                #this node as the current_node.
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
