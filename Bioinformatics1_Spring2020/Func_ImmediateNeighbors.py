def ImmediateNeighbors(Pattern):
    Neighborhood = [Pattern]
    nucleotides = ['A', 'C', 'G', 'T']
    for index in range(len(Pattern)):
        symbol = Pattern[index]
        for base in nucleotides:
            if base != symbol:
                neighbor = Pattern[:index] + base + Pattern[index + 1:]
                Neighborhood.append(neighbor)
    return Neighborhood
