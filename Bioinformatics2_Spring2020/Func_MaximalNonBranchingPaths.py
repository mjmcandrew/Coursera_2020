def MaximalNonBranchingPaths(graph):
    paths = []
    degrees = countDegrees(graph)
    for node in graph:
        print('start of new cycle with node ', node)
        print('start of new cycle with node degress ', degrees[node][0], degrees[node][1])
        if not (degrees[node][0] == 1 and degrees[node][1] == 1) and (degrees[node][0] > degrees[node][1]):
            print('this is not a 1-in 1-out node')
            print('this node has greater outdegree than indegree')
            for neighbor in graph[node]:#for neighbor in graph[node]:
                print('current node is ', node)
                print('initializing new non-branching path from this node...')
                nonBranchingPath = []
                print('appending initial node to non-branching path...')
                nonBranchingPath.append(node)
                print('non-branching path looks like ', nonBranchingPath)
                print('appending neighbor to non-branching path...')
                neighbor = graph[node].pop()
                print('neighbor is ', neighbor)
                nonBranchingPath.append(neighbor)
                print('non-branching path looks like ', nonBranchingPath)
                #if neighbor in graph.keys():
                    #print('neighbors neighbor is: ', graph[neighbor])
                    #print('neighbor indegree is: ', degrees[neighbor][1])
                while (degrees[neighbor][0] == 1) and (degrees[neighbor][1] == 1):
                    print('neighbor meets criteria')
                    print('neighborhood is, ', graph[neighbor])
                    neighbor = graph[neighbor].pop()
                    print('neighbor is ', neighbor)
                    nonBranchingPath.append(neighbor)
                    print('nonBranchingPath looks like ', nonBranchingPath)
                paths.append(nonBranchingPath)
    for node in graph:
        for neighbor in graph[node]:
        #print('neighbor is ', neighbor)
            nonBranchingPath = []
            nonBranchingPath.append(node)
            neighbor = graph[node].pop()
            nonBranchingPath.append(neighbor)
        #print('nonBranchingPath looks like ', nonBranchingPath)
            while (degrees[neighbor][0] == 1 and degrees[neighbor][1] == 1):
                if graph[neighbor]:
                    neighbor = graph[neighbor].pop()
                    #print('neighbor is ', neighbor)
                    nonBranchingPath.append(neighbor)
                    #print('nonBranchingPath looks like ', nonBranchingPath)
                else:
                    break
            paths.append(nonBranchingPath)
    return paths

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

with open("MaximalNonBranchingPaths.txt") as f:
    Input_graph = dict(line.strip().split(' -> ') for line in f)
    graph = {}
    for key, value in Input_graph.items():
        graph[key] = [val for val in value.split(',')]
print('graph is:\n', graph)
print('degrees are:\n', countDegrees(graph))
result = MaximalNonBranchingPaths(graph)
for path in result:
    print('->'.join([str(val) for val in path]))
