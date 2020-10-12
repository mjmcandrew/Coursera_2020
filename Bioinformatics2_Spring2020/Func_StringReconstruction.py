def StringReconstruction(Patterns):
    #This algorithm reconstructs a string given a set of kmers (reads).
    deBruijn = deBruijnFromKmers(Patterns)
    #Generates a deBruijn graph from the input kmers.
    eulerianPath = EulerianPath(deBruijn)
    #Finds a Eulerian path from the generated deBruijn graph.
    genome = PathToGenome(eulerianPath)
    #Reconstructs the genome inferred from the input kmers using
    #the Eulerian path.
    return genome

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
