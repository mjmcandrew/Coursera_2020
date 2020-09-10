import random

def EulerianCycle(graph, path = None, unexplored = None, current_node = None, target_node = None):
    print('initializing EulerianCycle with path = {path}, unexplored = {unexplored}, current_node = {current_node}, target_node = {target_node}'.format(path = path, unexplored = unexplored, current_node = current_node, target_node = target_node))
    cycle = []
    if path is None:
        path = []
        print('initial path is: ', path)
    if unexplored is None:
        unexplored = []
        for key in graph:
            unexplored.append(key)
        print('initial unexplored is: ', unexplored)
    if current_node is None:
        current_node = random.choice(list(graph))
        target_node = current_node
        print('initial starting/target node is: ', current_node)
    print('adding current node to path...')
    path.append(current_node)
    print('new path is: ', path)
    while unexplored:
        print('finding neighbors...')
        if graph[current_node]:
            if len(graph[current_node]) == 1:
                print('this node only has one adjacency. removing from unexplored')
                unexplored.remove(current_node)
                print('new unexplored is: ', unexplored)
            neighbor = graph[current_node].pop()
            print('neighbor is ', neighbor)
            print('graph is ', graph)
            current_node = neighbor
        else:
            #need to fix the logic here so that it backtracks or something
            print('dead end. reinitializing...')
            #break
            cycle = None
            unexplored = None
            current_node = None
            target_node = None
        return EulerianCycle(graph, path, unexplored, current_node, target_node)
    return path, cycle

if __name__ == "__main__":
    import sys
    Input = sys.stdin.readlines()
    Input_graph = dict(line.strip().split(' -> ') for line in Input)
    graph = {}
    for key, value in Input_graph.items():
        graph[int(key)] = [int(val) for val in value.split(',')]

print(graph)
result = EulerianCycle(graph)
#print('->'.join([str(val) for val in result]))
