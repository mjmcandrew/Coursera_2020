import random

def EulerianCycle(graph):
    cycle = []
    path = []
    current_node = random.choice(list(graph))
    path.append(current_node)
    while path:
        if graph[current_node]:
            neighbor = graph[current_node].pop()
            current_node = neighbor
            path.append(current_node)
        else:
            cycle.append(path.pop())
            if path:
                current_node = path[-1]
    return cycle[::-1]


with open("EulerianCycle.txt") as f:
    Input_graph = dict(line.strip().split(' -> ') for line in f)
    graph = {}
    for key, value in Input_graph.items():
        graph[key] = [val for val in value.split(',')]



result = EulerianCycle(graph)
print('->'.join([str(val) for val in result]))
