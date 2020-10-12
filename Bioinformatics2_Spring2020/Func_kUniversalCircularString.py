import itertools
import random

def kUniversalCircularString(k):
    #Given an integer 'k', this algorithm generates a k universal circular
    #string, a string which contains all binary kmers exactly once. For example,
    #a possible 3-universal string is 00011101, as it contains all possible
    #binary 3-mers 000, 001, 011, 111, 110, 101, 010, and 100 exactly once.
    binary_strings = generateBinaryStrings(k)
    #Generates all binary strings possible given length 'k'.
    binary_deBruijn = deBruijnFromKmers(binary_strings)
    #Generates a deBruijn graph from the binary strings generated.
    binary_cycle = EulerianCycle(binary_deBruijn)
    #Generates a Eulerian cyclce from the deBruijn graph.
    circular_string = PathToGenome(binary_cycle)
    #Reconstructs a string from the Eulerian cycle. Note that the output will
    #not account for the circularity of the string, so the final kmer is
    #removed before returning the string.
    return circular_string[: len(circular_string) - k + 1]

def generateBinaryStrings(k):
    #This algorithm uses itertools to generate all possible unique combinations
    #of the binary digits 0 and 1 given size k. For example, given k = 2, this
    #sub-algorithm will generate 00, 01, 10, and 11.
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
