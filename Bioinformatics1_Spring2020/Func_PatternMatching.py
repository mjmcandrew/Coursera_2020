def PatternMatching(Pattern, Genome):
    #Finds and returns the starting index positions within string
    #'Genome' where the input 'Pattern' appears.
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions
