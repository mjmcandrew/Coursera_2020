import sys
def GraphFromAdjacencies():
    Input = sys.stdin.readlines()
    Input_graph = dict(line.strip().split(' -> ') for line in Input)
    graph = {}
    for key, value in Input_graph.items():
        graph[int(key)] = [int(val) for val in value.split(',')]

print(graph)
