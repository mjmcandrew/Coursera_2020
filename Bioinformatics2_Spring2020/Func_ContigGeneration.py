def ContigGeneration(Patterns):
    #This algorithm generates contigs (or maximal non-branching paths) from a
    #collection of kmers. In real-world terms, this allows biologists to use
    #sequencing data which may be impossible to completely reconstruct due to
    #repeats or errors.
    contigs = []
    #Initializes the empty list 'contigs'.
    graph = deBruijnFromKmers(Patterns)
    #Generates a deBruijn graph from input kmers.
    paths = MaximalNonBranchingPaths(graph)
    #Generates all maximal non-branching paths present in the graph.
    for path in paths:
        contig = PathToGenome(path)
        #Given a maximal non-branching path, this uses PathToGenome to generate
        #a string from the kmers present in this path and adds it to 'contigs'.
        contigs.append(contig)
    return contigs

def MaximalNonBranchingPaths(graph):
    #This algorithm takes a deBruijn graph as input and returns all maximal non-branching
    #paths. For example, given the graph {1: [2], 2: [3], 3: [4, 5], 6: [7], 7: [6]},
    #the algorithm returns:
    #1 -> 2 -> 3
    #3 -> 4
    #3 -> 5
    #7 -> 6 -> 7 (or 6 -> 7 -> 6)
    paths = []
    #Initializes the empty list 'paths'.
    degrees = countDegrees(graph)
    #Returns indegree and outdegree of all nodes in the input graph.
    for node in graph:
        #Iterates through nodes in the graph.
        if not (degrees[node][0] == 1 and degrees[node][1] == 1) and (degrees[node][0] > 0):
            #Determines whether the node is NOT a 1-in 1-out node and whether the
            #node has outdegree.
            while graph[node]:
                #Initializes a while loop that will continue as long as the current
                #node has outdegree.
                nonBranchingPath = []
                #Initializes the empty list 'nonBranchingPath'.
                nonBranchingPath.append(node)
                #Adds currend node to the non-branching path.
                neighbor = graph[node].pop()
                #'Pops' the edge connecting the current node to its outdegree
                #neighbor and assigns it to neighbor before adding the neighbor
                #node to the non-branching path.
                nonBranchingPath.append(neighbor)
                while (degrees[neighbor][0] == 1) and (degrees[neighbor][1] == 1):
                    #Determines whether the neighbor node is a 1-in 1-out node. As
                    #long as it is, the while loop will continue, reassigning
                    #'neighbor' to the next node and adding this node to the
                    #non-branching path.
                    neighbor = graph[neighbor].pop()
                    nonBranchingPath.append(neighbor)
                paths.append(nonBranchingPath)
                #At the conclusion of the while loop, the non-branching path
                #is added to 'paths'.
    for node in graph:
        #This portion of the code finds Eulerian cycles that may be present
        #in remaining nodes that do not fit the criteria above.
        if graph[node]:
        #Determines whether the current node has outdegree.
            path = []
            cycle = []
            path.append(node)
            #Initializes the empty lists 'path' and 'cycle' and adds the
            #current node to path.
            while path:
                #Initializes a while loop that will continue as long as 'path'
                #contains nodes.
                if node not in graph.keys():
                    #If the current node is not in the graph's keys, and thus
                    #has no outdegree, it is removed from path and added to cycle.
                    #The algorithm then backtracks to the previous node.
                    cycle.append(path.pop())
                    if path:
                        node = path[-1]
                if graph[node]:
                    #If the current node has a neighbor, the neighbor is removed
                    #from adjacencies and becomes the current node, which is added
                    #to path.
                    neighbor = graph[node].pop()
                    node = neighbor
                    path.append(node)
                else:
                    #If the node does not have neighbors, it is removed from path
                    #and added to cycle. The algorithm then backtracks to the previous
                    #node and begins the while loop again.
                    cycle.append(path.pop())
                    if path:
                        node = path[-1]
            paths.append(cycle[::-1])
            #At the conclusion of the while loop, the cycle is added to paths.
    return paths

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

with open("ContigGeneration.txt") as f:
    input = f.readlines()
    patterns =[x.strip() for x in input]

print(patterns)

#import sys
#if __name__ == "__main__":
    #Input = sys.stdin.readlines()
    #patterns = [pattern.strip() for pattern in Input]


result = ContigGeneration(patterns)
print(' '.join(result))
