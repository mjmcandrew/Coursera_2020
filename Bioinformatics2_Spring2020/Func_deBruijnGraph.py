def deBruijnGraph(k, Text):
    pathGraph = {}
    #Creates an empty dictionary which will store nodes and values
    #associated with those nodes.
    node_length = k - 1
    #Sets node_length equal to the k value given minus 1.
    for index in range(len(Text) - node_length):
        #Iterates through each index in the text given.
        node = Text[index:index + node_length]
        #Captures 'nodes' from Text equal to the length of k - 1.
        pathGraph[node] = []
        #Establishes each node as a key in the pathGraph dictionary and sets
        #its value equal to an empty list.
    for index in range(len(Text) - node_length):
        #Iterates through each index in the text given allowing for node length.
        node = Text[index:index + k - 1]
        #Captures the node in the string of text.
        partner_node = Text[index + 1: index + k]
        #Captures 'partner_node', the node that is adjacent to the previous
        #node captured.
        pathGraph[node].append(partner_node)
        #Adds partner_node to the empty list of values associated with the
        #'node' key.
    return pathGraph
