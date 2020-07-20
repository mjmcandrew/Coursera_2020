def RandomMotifs(Dna, k, t):
    import random
    RandomMotifs = []
    #Creates the empty set 'RandomMotifs'.
    for Dna_string in Dna:
        #Iterates through the strings in 'Dna'
        random_index = random.randint(0, (len(Dna_string) - k))
        #Generates a random index that will serve as a starting point
        #allowing for the length of desired kmer.
        random_motif = Dna_string[random_index:random_index+k]
        #Generates a random motif using the random index as the starting
        #point and allows for the length of k.
        RandomMotifs.append(random_motif)
        #Adds randomly generated motif to set 'RandomMotifs'.
    return RandomMotifs
