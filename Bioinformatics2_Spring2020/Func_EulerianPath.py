def EulerianPath(graph):
    degrees = countDegrees(graph)
    #Determine start node and end node based on Eulerian principles.
    print('degrees are ', degrees)
    for node in degrees:
        if (degrees[node][0] - degrees[node][1]) == 1:
            start_node = node
        elif (degrees[node][1] - degrees[node][0]) == 1:
            end_node = node
    if not start_node or not end_node:
        return "Graph is not Eulerian!"
    print('start_node is ', start_node)
    print('end_node is ', end_node)
    if end_node not in graph.keys():
        graph[end_node] = [start_node]
    else:
        graph[end_node].append(start_node)
    print('new graph is ', graph)
    path = []
    cycle = []
    path.append(start_node)
    current_node = start_node
    print('type of node is', type(current_node))
    print('type of nodes pointies is ', type(graph[current_node]))
    while path:
        if graph[current_node]:
            print('current node is ', current_node)
            print('neighbors are ', graph[current_node])
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
    #Could try separating this out to indegrees and outdegrees. Could also make this a tuple. #thingstotry
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

def convertDegrees(degrees):
    numeric_degrees = {}
    for key in degrees:
        numeric_key = PatternToNumber(key)
        numeric_degrees[numeric_key] = degrees[key]
    return numeric_degrees

def convertGraph(graph):
    converted_graph = {}
    for key in graph:
        numeric_key = int(PatternToNumber(key))
        converted_graph[numeric_key] = []
        for value in graph[key]:
            print('value is ', value)
            converted_value = int(PatternToNumber(value))
            print('converted value is ', converted_value)
            converted_graph[numeric_key].append(converted_value)
            print('converted graph is ', converted_graph)
    return converted_graph



def PatternToNumber(pattern):
    base4 = {}       # This creates the dictionary that will be used to convert
    base4['A'] = 0   # a DNA base string to a number.
    base4['C'] = 1
    base4['G'] = 2
    base4['T'] = 3
    n = len(pattern)
    number = 0
    if n == 0: #Ensures that user has entered a DNA base string.
        return "You have not entered a string."
    for character in range(n):
        number += base4[pattern[character]] * (4 ** (n - character - 1))
        # Note: "character" is required as part of the "n - ..." equation
        # because "character" acquires the index value of the character inside
        # the string. For instance, in a string "AGT", character would be
        # assigned as A = 0, G = 1, T = 2, while the value of n does not
        # change.
    return number

with open("EulerianPath.txt") as f:
    Input_graph = dict(line.strip().split(' -> ') for line in f)
    graph = {}
    for key, value in Input_graph.items():
        graph[key] = [val for val in value.split(',')]
print('graph is ', graph)
#converted_graph = convertGraph(graph)
result = EulerianPath(graph)
print('->'.join([str(val) for val in result]))
