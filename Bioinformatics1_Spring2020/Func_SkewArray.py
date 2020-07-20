def SkewArray(Genome):
    skew = [''] * (len(Genome) + 1)
    skew[0] = 0
    skewValue = 0
    n = len(Genome)
    for index in range(n):
        if Genome[index] == 'G':
            skewValue += 1
            skew[index + 1] = skewValue
        if Genome[index] == 'C':
            skewValue -= 1
            skew[index + 1] = skewValue
        else:
            skew[index + 1] = skewValue
    return skew
