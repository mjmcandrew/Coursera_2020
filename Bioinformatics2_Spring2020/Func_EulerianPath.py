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
            print(type(graph[current_node]))
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
        #Note: May need to switch positions of indegrees and outdegrees at some point.
    return degrees

with open("EulerianPath.txt") as f:
    Input_graph = dict(line.strip().split(' -> ') for line in f)
    graph = {}
    for key, value in Input_graph.items():
        graph[key] = [val for val in value.split(',')]
print('graph is ', graph)
#converted_graph = convertGraph(graph)
result = EulerianPath(graph)
print('->'.join([str(val) for val in result]))
