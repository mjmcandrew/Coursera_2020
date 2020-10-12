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
